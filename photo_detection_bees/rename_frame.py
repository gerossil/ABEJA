import os

def rename_photos(folder_path, special_name):
    counter = 1
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            extension = os.path.splitext(filename)[1]
            new_name = f"{special_name}_{counter}{extension}"
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            counter += 1

if __name__ == "__main__":
    folder_path = "C:\\Users\\UMFRAB\\Documents\\ABEJA\\photo_detection_bees\\bees\\bees_v8"  # Remplacez cela par le chemin de votre dossier
    special_name = "bees_v8"  # Remplacez cela par le nom spécial souhaité
    rename_photos(folder_path, special_name)
