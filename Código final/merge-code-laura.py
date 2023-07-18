import cv2
import numpy as np
import math
import time
from detectar_mov_area4 import procesarVideo
from Hole import Hole



def main():
    start_time = time.time()

    # Ouvrir la vidéo
    video = 'C:\\Users\\LABSIS\\Documents\\ABEJA\\photo_tracking\\video-zoomed.mp4'


    capture = cv2.VideoCapture(video)


    ret, first_frame = capture.read()
    cv2.imshow("Detected Circle", first_frame)

    circles_tab = []
    peripherical_circles_tab = [] #to assume bees are getting out, we'll need to check the periphery of the hole
    
    for i in range(1):
        ret, frame = capture.read()

        if ret:
            holes_count = 0
            # Convert to grayscale.
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Blur using 3 * 3 kernel.
            gray_blurred = cv2.blur(gray, (14, 14))

            # Apply Hough transform on the blurred image.
            detected_circles = cv2.HoughCircles(gray_blurred, 
                            cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
                        param2 = 25, minRadius = 0, maxRadius = 50)
            
            # Draw circles that are detected.
            if detected_circles is not None:
            
                # Convert the circle parameters a, b and r to integers.
                detected_circles = np.uint16(np.around(detected_circles))
            
                for pt in detected_circles[0, :]:
                    a, b, r = pt[0], pt[1], pt[2]
                    #print("trying to add circles at a : " + str(a) + " b : " + str(b) + " r : " + str(r))

                    if len(circles_tab) == 0:
                        circles_tab.append(Hole("Hoyo"+str(holes_count),a,b,r+5))#Radius + 5 to have a little bit larger area
                        peripherical_circles_tab.append(Hole("Hoyo"+str(holes_count),a,b,r+15))
                        holes_count += 1
                        #print("added first")
                        # Draw the circumference of the circle.
                        cv2.circle(first_frame, (a, b), r, (0, 255, 0), 2)
                
                        # Draw a small circle (of radius 1) to show the center.
                        cv2.circle(first_frame, (a, b), 1, (0, 0, 255), 3)

                    else:
                        inside = False
                        for circle in circles_tab:
                            if circle.areCirclesSuperimposed(a,b,r+5):
                                inside = True
                                break
                        
                        if inside == False:
                            circles_tab.append(Hole("Hoyo"+str(holes_count),a,b,r+5))
                            peripherical_circles_tab.append(Hole("Hoyo"+str(holes_count),a,b,r+15))
                            holes_count += 1   
                            # Draw the circumference of the circle.
                            cv2.circle(first_frame, (a, b), r, (0, 255, 0), 2)
                    
                            # Draw a small circle (of radius 1) to show the center.
                            cv2.circle(first_frame, (a, b), 1, (0, 0, 255), 3)

    end_time = time.time()
    exec_time = end_time - start_time

    print("exec_time : ", exec_time)

    cv2.imshow("Detected Circle", first_frame)
    cv2.waitKey(0)

    procesarVideo(circles_tab, peripherical_circles_tab, video)


      

if __name__ == "__main__":
    main()



    