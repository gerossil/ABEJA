from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import os
import numpy as np


# Exemple de données de requête de flux
video_name = "My Video"
fps = 30
date_range = "2023-07-13 10:00:00 - 2023-07-13 11:00:00"
photo_path = "/Users/malcolmneerman/dev/Abeja/ABEJA/server/services/IMG_2238.jpeg"

# Exemple de données pour le graphe (vous pouvez remplacer ces valeurs par les données de votre base de données)
x_values = [1, 2, 3, 4, 5]
y_values = [10, 20, 15, 30, 25]
matplotlib.use('agg')
data = []

# Créer le graphe avec Matplotlib
def create_graph():
  import datetime
  with open('C:\\Users\\UMFRAB\\Documents\\ABEJA\\server\\bees-datas.csv', 'r') as csv_file:
    for line in csv_file:
      try :
        parts = line.strip().split(',')

        print(parts)
        
        entry_str = parts[0].split(' : ')[1]
        exit_str = parts[1].split(' : ')[1]
        duration_str = parts[2].split(': ')[1]
        hoyo_str = parts[3].split(': ')[1]

        print(entry_str)
        
        entry_time = datetime.datetime.strptime(entry_str, '%Y-%m-%d %H:%M:%S.%f')
        exit_time = datetime.datetime.strptime(exit_str, '%Y-%m-%d %H:%M:%S.%f')
        
        duration_parts = duration_str.split(':')
        duration_timedelta = datetime.timedelta(hours=int(duration_parts[0]), minutes=int(duration_parts[1]), seconds=int(duration_parts[2]))
        duration_seconds = duration_timedelta.total_seconds()
        
        data.append({
            'entry_time': entry_time,
            'exit_time': exit_time,
            'duration_seconds': duration_seconds,
            'hoyo': hoyo_str
        })
      except : 
        pass

  # Créer le graphique à barres
  
  hours = [timestamp['entry_time'].hour + timestamp['entry_time'].minute / 60 for timestamp in data]
  durations = [entry['duration_seconds'] for entry in data]

  plt.bar(hours, durations)
  plt.xlabel("Observation Time (24 Hours)")
  plt.ylabel("Dwell time (seconds)")
  plt.title("Dwell time in each hole")
  plt.xticks(range(1, 25))  # Échelle horaire de 0 à 24 heures
  plt.savefig("graph.png")

# Créer le PDF avec ReportLab
def create_pdf(video_name, fps, date_range, photo, holes_count, closed_holes_count):
    if os.path.exists("output.pdf"):
      os.remove("output.pdf")
    pdf_file = "output.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)

    # Ajouter l'en-tête au PDF
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 750, "Video Name: " + video_name)
    c.drawString(100, 730, "Frame Per Second: " + str(np.around(fps)))
    c.drawString(100, 710, "Date: " + date_range)

    filename = 'temp_photo.jpg'
    cv2.imwrite(filename, photo)
     # Charger l'image avec PIL
    image = Image.fromarray(cv2.cvtColor(photo, cv2.COLOR_BGR2RGB))  
    img_width, img_height = image.size

  # Calculer la hauteur proportionnelle à la largeur pour occuper toute la largeur du PDF
    target_width = letter[0] - 200
    target_height = (target_width * img_height) // img_width

    # Dessiner l'image avec la taille calculée
    c.drawString(100, 680, "Nest and holes: " + str(holes_count) + " open holes and " + str(closed_holes_count) + " closed holes" )
    c.drawImage(filename, 100, 710 - target_height - 50, width=target_width, height=target_height)

    # Générer le graphe
    create_graph()

    # Ajouter le graphe au PDF
    c.drawString(100, 710 - target_height - 100, "Graph:")
    c.drawInlineImage("graph.png", 100, 100, width=400, height=250)


    c.save()
    print(f"PDF généré : {pdf_file}")

# Exécuter la fonction pour créer le PDF
#create_pdf(video_name, fps, date_range, photo_path)
