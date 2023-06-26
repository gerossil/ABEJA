import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    chemin_video = "C:\\Users\\DEPTEC\\Documents\\abejas\\ABEJA\\videos\\Bees-Cajica-1.MOV"

    # Ouvrir la vidéo
    capture = cv2.VideoCapture(chemin_video)

    # Lire la première frame
    _, frame = capture.read()

    # Prétraitement de l'image
    image = cv2.GaussianBlur(frame, (5, 5), 0)

    # Détection des cercles
    circles = cv2.HoughCircles(frame, cv2.HOUGH_GRADIENT, dp=1, minDist=10, param1 = 50,
                    param2 = 25, minRadius=5, maxRadius=50)

    # Dessin des cercles détectés sur l'image
    if circles is not None:
        circles = np.round(circles[0, :]).astype(int)
        for (x, y, r) in circles:
            cv2.circle(image, (x, y), r, (0, 255, 0), 2)

    # Affichage de l'image résultante
    cv2.imshow("Cercles détectés", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()