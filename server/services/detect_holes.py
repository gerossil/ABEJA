import cv2
import numpy as np
import time
import services.detect_bees as detect_bees
from services.Hole import Hole
from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt
import tempfile

#hole detection function, returns an array of the holes detected, the temporary video to analyse, and the first frame picture
def detectHoles(video):
    
    start_time = time.time()
    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp_file:
        temp_file.write(video.read())
        temp_file_path = temp_file.name

        capture = cv2.VideoCapture(temp_file_path)
        ret, first_frame = capture.read()

        # Load the model
        model = YOLO('./yolo/model-holes.pt')  # load a pretrained model
        results = model(first_frame) #parse the image to get the holes

        boxes = results[0].boxes.xyxy.tolist()
        holes_count = 0
        circles_tab = []
        circles_done_tab = []

        for box in boxes: 
            x_min, y_min, x_max, y_max = box
            class_id = results[0].names[results[0].boxes[holes_count].cls[0].item()] #get type of objects in image (hole, holeDone, hotel)
            if class_id == "Hole":
                center_x =  np.uint16(np.around((x_min + x_max) / 2))
                center_y = np.uint16(np.around((y_min + y_max) / 2))
                radius = np.uint16(np.around((x_max - x_min) / 2))
                circles_tab.append(Hole("Hoyo" + str(holes_count), center_x, center_y, radius * 1.10))#Radius + 5 to have a little bit larger area
                #Draw circles with point at the center
                cv2.circle(first_frame, (center_x, center_y), radius, (0, 255, 0), 2)
                cv2.circle(first_frame, (center_x, center_y), 1, (0, 0, 255), 3)
                

            if class_id == "HoleDone":
                center_x =  np.uint16(np.around((x_min + x_max) / 2))
                center_y = np.uint16(np.around((y_min + y_max) / 2))
                radius = np.uint16(np.around((x_max - x_min) / 2))
                circles_done_tab.append(Hole("Hoyo" + str(holes_count), center_x, center_y, radius * 1.10))#Radius + 5 to have a little bit larger area
                #Draw circles with point at the center
                cv2.circle(first_frame, (center_x, center_y), radius, (255, 0, 0), 2)
                cv2.circle(first_frame, (center_x, center_y), 1, (0, 0, 255), 3)
            holes_count += 1

        end_time = time.time()
        exec_time = end_time - start_time

        print("exec_time : ", exec_time)
        return circles_tab, circles_done_tab, temp_file_path, first_frame
    
        detect_bees.procesarVideo(circles_tab, temp_file_path)
  


    