from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
from io import BytesIO
import datetime
from PIL import Image
import cv2

# Exemple de données de requête de flux
video_name = "My Video"
fps = 30
date_range = "2023-07-13 10:00:00 - 2023-07-13 11:00:00"
photo_path = "/Users/malcolmneerman/dev/Abeja/ABEJA/server/services/IMG_2238.jpeg"

# Exemple de données pour le graphe (vous pouvez remplacer ces valeurs par les données de votre base de données)
x_values = [1, 2, 3, 4, 5]
y_values = [10, 20, 15, 30, 25]

# Créer le graphe avec Matplotlib
def create_graph():
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Sample Graph')
    plt.grid(True)
    plt.savefig("graph.png")

# Créer le PDF avec ReportLab
def create_pdf(video_name, fps, date_range, photo):
    pdf_file = "output.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)

    # Ajouter l'en-tête au PDF
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 750, "Video Name: " + video_name)
    c.drawString(100, 730, "Frame Per Second: " + str(fps))
    c.drawString(100, 710, "Date: " + date_range)

     # Charger l'image avec PIL
    img = Image.fromarray(cv2.cvtColor(photo, cv2.COLOR_BGR2RGB))

    img_width, img_height = img.size
  # Calculer la hauteur proportionnelle à la largeur pour occuper toute la largeur du PDF
    target_width = letter[0] - 200
    target_height = (target_width * img_height) // img_width

    # Dessiner l'image avec la taille calculée
    c.drawString(100, 680, "Nest and holes:")
    c.drawImage(photo, 100, 710 - target_height - 50, width=target_width, height=target_height)

    # Générer le graphe
    create_graph()

    # Ajouter le graphe au PDF
    c.drawString(100, 710 - target_height - 100, "Graph:")
    c.drawInlineImage("graph.png", 100, 100, width=400, height=250)


    c.save()
    print(f"PDF généré : {pdf_file}")

# Exécuter la fonction pour créer le PDF
#create_pdf(video_name, fps, date_range, photo_path)
