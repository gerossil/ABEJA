import cv2
import numpy as np

def main():
    #chemin_video = "C:\\Users\\DEPTEC\\Documents\\abejas\\ABEJA\\videos\\Bees-Cajica-1.MOV"

    image = cv2.imread("C:\\Users\\DEPTEC\\Documents\\abejas\\ABEJA\\photo\\pantalla.png", 0)  # Chargez l'image en niveaux de gris

    image = cv2.GaussianBlur(image, (5, 5), 0)  # Appliquez un flou gaussien pour réduire le bruit

    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=25, minRadius=100, maxRadius=1000)


    
    # Draw circles that are detected.
    if circles is not None:
    
        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(circles))
    
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
    
            # Draw the circumference of the circle.
            cv2.circle(image, (a, b), r, (0, 255, 0), 2)
    
            # Draw a small circle (of radius 1) to show the center.
            #cv2.circle(image, (a, b), 1, (0, 0, 255), 3)

            
    cv2.imshow("Detected Circle", image)
    cv2.waitKey(0)


      

if __name__ == "__main__":
    main()



    