import cv2
import numpy as np

# Chargement de l'image
image = cv2.imread("C:\\Users\\DEPTEC\\Documents\\abejas\\ABEJA\\photo\\premiere_frame.jpg", 0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Prétraitement de l'image
image = cv2.GaussianBlur(gray, (3, 3), 0)

# Détection des contours
#edges = cv2.Canny(image, threshold1=20, threshold2=100)

# Détection des cercles avec une plage de rayon variable
min_radius = 5
max_radius = 50
circles = cv2.HoughCircles(image,  cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
                    param2 = 25, minRadius = 5, maxRadius = 50)

# Dessin des cercles détectés sur l'image
if circles is not None:
    circles = np.round(circles[0, :]).astype(int)
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)

# Affichage de l'image résultante
cv2.imshow("Cercles détectés", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
