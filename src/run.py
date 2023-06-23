import cv2
import numpy as np

def main():
    chemin_video = "C:\\Users\\DEPTEC\\Documents\\abejas\\ABEJA\\videos\\Bees-Cajica-1.MOV"

    # Ouvrir la vidéo
    capture = cv2.VideoCapture(chemin_video)

    # Lire la première frame
    ret, frame = capture.read()

    # Vérifier si la lecture de la frame a réussi
    if ret:
                
        # Convert to grayscale.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray", gray)

        # Blur using 3 * 3 kernel.
        gray_blurred = cv2.blur(gray, (15, 15))
        
        # Apply Hough transform on the blurred image.
        detected_circles = cv2.HoughCircles(gray_blurred, 
                        cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
                    param2 = 25, minRadius = 5, maxRadius = 50)
        
        # Draw circles that are detected.
        if detected_circles is not None:
        
            # Convert the circle parameters a, b and r to integers.
            detected_circles = np.uint16(np.around(detected_circles))
        
            for pt in detected_circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]
        
                # Draw the circumference of the circle.
                cv2.circle(frame, (a, b), r, (0, 255, 0), 2)
        
                # Draw a small circle (of radius 1) to show the center.
                cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)

                 # Sauvegarder la frame en tant qu'image
        cv2.imwrite("premiere_frame.jpg", frame)
        cv2.imshow("Detected Circle", frame)
        cv2.waitKey(0)


      

if __name__ == "__main__":
    main()



    