import cv2
import numpy as np


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    
    def areCirclesSuperimposed(self, point_x, point_y, radius):
        dist_x = point_x - self.x if point_x > self.x else self.x - point_x
        dist_y = point_y - self.y if point_y > self.y else self.y - point_y

        distance = dist_x**2 + dist_y**2
        somme_rayons = radius + self.radius

        if distance <= somme_rayons**2:
            return True
        else:
            return False
        

chemin_video = "C:\\Users\\DEPTEC\\Documents\\abejas\\ABEJA\\videos\\CuartaToma.mp4"

# Ouvrir la vidéo
capture = cv2.VideoCapture(chemin_video)

# Lire la première frame
ret, raw_image = capture.read()
first_frame = raw_image

circles_tab = []

# Vérifier si la lecture de la frame a réussi
if ret:
    cv2.imshow('Original Image', raw_image)
    cv2.waitKey(0)

    bilateral_filtered_image = cv2.bilateralFilter(raw_image, 5, 175, 175)
    cv2.imshow('Bilateral', bilateral_filtered_image)
    cv2.waitKey(0)

    gray_blurred = cv2.blur(bilateral_filtered_image, (5, 5))
    edge_detected_image = cv2.Canny(gray_blurred, 75, 200)
    cv2.imshow('Edge', edge_detected_image)
    cv2.waitKey(0)

    # _, contours = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # contour_list = []
    # for contour in contours:
    #     approx = cv2.approxPolyDP(contour,0.01 * cv2.arcLength(contour,True),True)
    #     area = cv2.contourArea(contour)
    #     if ((len(approx) > 8) & (len(approx) < 23) & (area > 30) ):
    #         contour_list.append(contour)

    # cv2.drawContours(raw_image, contour_list,  -1, (255,0,0), 2)

    detected_circles = cv2.HoughCircles(edge_detected_image, 
                            cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
                        param2 = 25, minRadius = 1, maxRadius = 50)
            
    # Draw circles that are detected.
    if detected_circles is not None:
    
        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))
    
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            #print("trying to add circles at a : " + str(a) + " b : " + str(b) + " r : " + str(r))

            if len(circles_tab) == 0:
                circles_tab.append(Circle(a,b,r))
                #print("added first")
                # Draw the circumference of the circle.
                cv2.circle(first_frame, (a, b), r, (0, 255, 0), 2)
        
                # Draw a small circle (of radius 1) to show the center.
                cv2.circle(first_frame, (a, b), 1, (0, 0, 255), 3)

            else:
                inside = False
                for circle in circles_tab:
                    if circle.areCirclesSuperimposed(a,b,r):# or circle.isPointInside(a,b):
                        inside = True
                        break
                
                if inside == False:
                    circles_tab.append(Circle(a,b,r))
                    # print("added new")
                    # Draw the circumference of the circle.
                    cv2.circle(first_frame, (a, b), r, (0, 255, 0), 2)
            
                    # Draw a small circle (of radius 1) to show the center.
                    cv2.circle(first_frame, (a, b), 1, (0, 0, 255), 3)

                    
    cv2.imshow('Objects Detected',raw_image)
    cv2.waitKey(0)