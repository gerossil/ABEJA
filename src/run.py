import cv2
import numpy as np
import math
import time

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def isInside(self, point_x, point_y):
        distance = (point_x - self.x)^2 + (point_y - self.y)^2
        print("le cercle x : " + str(point_x) + ", y : " + str(point_y) + " est il dans self x : " + str(self.x) + ", self y : " + str(self.y) + ", self r : " + str(self.radius))
        print("distance : " + str(distance) + " radius : " + str(self.radius))
        print(str(distance <= self.radius^2))
        return distance <= self.radius^2

def main():
    chemin_video = "C:\\Users\\DEPTEC\\Documents\\abejas\\ABEJA\\videos\\CuartaToma.mp4"

    # Ouvrir la vidéo
    capture = cv2.VideoCapture(chemin_video)

    # Lire la première frame
    
    ret, first_frame = capture.read()

    circles_tab = []
    
    for i in range(10):
        ret, frame = capture.read()

        # Vérifier si la lecture de la frame a réussi
        if ret:
                    
            # Convert to grayscale.
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Blur using 3 * 3 kernel.
            gray_blurred = cv2.blur(gray, (15, 15))

            # Apply Hough transform on the blurred image.
            detected_circles = cv2.HoughCircles(gray_blurred, 
                            cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
                        param2 = 25, minRadius = 1, maxRadius = 50)
            
            # Draw circles that are detected.
            if detected_circles is not None:
            
                # Convert the circle parameters a, b and r to integers.
                detected_circles = np.uint16(np.around(detected_circles))
            
                for pt in detected_circles[0, :]:
                    a, b, r = pt[0], pt[1], pt[2]
                    print("trying to add circles at a : " + str(a) + " b : " + str(b) + " r : " + str(r))

                    if len(circles_tab) == 0:
                        circles_tab.append(Circle(a,b,r))
                        print("added first")
                        # Draw the circumference of the circle.
                        cv2.circle(first_frame, (a, b), r, (0, 255, 0), 2)
                
                        # Draw a small circle (of radius 1) to show the center.
                        cv2.circle(first_frame, (a, b), 1, (0, 0, 255), 3)

                    else:
                        inside = False
                        for circle in circles_tab:
                            if circle.isInside(a,b):
                                inside = True
                                break
                        
                        if inside == False:
                            circles_tab.append(Circle(a,b,r))
                            print("added new")
                            # Draw the circumference of the circle.
                            cv2.circle(first_frame, (a, b), r, (0, 255, 0), 2)
                    
                            # Draw a small circle (of radius 1) to show the center.
                            cv2.circle(first_frame, (a, b), 1, (0, 0, 255), 3)

                # Sauvegarder la frame en tant qu'image
    #cv2.imwrite("premiere_frame2.jpg", first_frame)
    cv2.imshow("Detected Circle", first_frame)
    cv2.waitKey(0)


      

if __name__ == "__main__":
    main()



    