import cv2
import numpy as np
import time
from detectar_mov_area4 import procesarVideo
from Hole import Hole
from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt


def main():
    
    start_time = time.time()
    # Ouvrir la vidéo
    capture = cv2.VideoCapture('C:\\Users\\DEPTEC\\Documents\\abejas\\ABEJA\\Código final\\nido.mp4')
    ret, first_frame = capture.read()

    # Load the model
    model = YOLO('C:\\Users\\DEPTEC\\Documents\\abejas\\ABEJA\\photo_detection\\runs\\detect\\train9\\weights\\best.pt')  # load a pretrained model
    results = model(first_frame) #parse the image to get the holes

    boxes = results[0].boxes.xyxy.tolist()
    holes_count = 0
    circles_tab = []
    peripherical_circles_tab = [] #to assume bees are getting out, we'll need to check the periphery of the hole

    for box in boxes: 
        x_min, y_min, x_max, y_max = box
        class_id = results[0].names[results[0].boxes[holes_count].cls[0].item()] #get type of objects in image (hole, holeDone, hotel)
        if class_id == "Hole":
            center_x =  np.uint16(np.around((x_min + x_max) / 2))
            center_y = np.uint16(np.around((y_min + y_max) / 2))
            radius = np.uint16(np.around((x_max - x_min) / 2))
            circles_tab.append(Hole("Hoyo" + str(holes_count), center_x, center_y, radius + 5))#Radius + 5 to have a little bit larger area
            peripherical_circles_tab.append(Hole("Hoyo" + str(holes_count), center_x, center_y, radius + 15))
            #Draw circles with point at the center
            cv2.circle(first_frame, (center_x, center_y), radius, (0, 255, 0), 2)
            cv2.circle(first_frame, (center_x, center_y), 1, (0, 0, 255), 3)
        holes_count += 1

    end_time = time.time()
    exec_time = end_time - start_time

    print("exec_time : ", exec_time)

    cv2.imshow("Detected Circle", first_frame)
    cv2.waitKey(0)

    procesarVideo(circles_tab, peripherical_circles_tab)
  

if __name__ == "__main__":
    main()



    