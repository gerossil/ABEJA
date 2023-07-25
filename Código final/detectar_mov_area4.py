import cv2
import numpy as np
import csv
import datetime
from typing import List
from Hole import Hole
from ultralytics import YOLO
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


def procesarVideo(holes: List[Hole], peripherical_holes: List[Hole], video):
    global cap, fgbg, kernel
    
    cap = cv2.VideoCapture(video)
    model = YOLO('C:\\Users\\DEPTEC\\Documents\\abejas\\ABEJA\\photo_detection_bees\\runs\\detect\\train2\\weights\\best.pt')  # load a pretrained model

    fgbg = cv2.createBackgroundSubtractorMOG2()
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = 0 #we need to count every frame to get the real time of entries and exits
    start_time = datetime.datetime.now()

    token = "my-token"
    org = "my-org"
    url = "http://localhost:8086"

    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

    bucket="my-bucket"

    write_api = client.write_api(write_options=SYNCHRONOUS)


    with open(f'abejas-prueba-{str(start_time).replace(" ","").replace(":","-").replace(".","-")}.csv', mode='w') as file:
        employee_writer = csv.writer(file, delimiter=',')

        while True:
            frame_count += 1
            ret, frame = cap.read()
            if ret == False: break
            results = model(frame)
            boxes = results[0].boxes.xyxy.tolist()
            holes_count = 0
            bees_tab = []

            for box in boxes: 
                x_min, y_min, x_max, y_max = box
                class_id = results[0].names[results[0].boxes[holes_count].cls[0].item()] #get type of objects in image (hole, holeDone, hotel)
                print(class_id)
                if class_id == "Bees":
                    center_x =  np.uint16(np.around((x_min + x_max) / 2))
                    center_y = np.uint16(np.around((y_min + y_max) / 2))
                    radius = np.uint16(np.around((x_max - x_min) / 2))
                    bees_tab.append(Hole("bee" + str(holes_count), center_x, center_y, radius + 5))#Radius + 5 to have a little bit larger area
                    #Draw circles with point at the center
                    cv2.circle(frame, (center_x, center_y), radius, (0, 255, 0), 2)

                    holes_count += 1
                    for i, h in enumerate(holes):
                        if h.isPointInside(center_x, center_y):#if bee is inside one of the hole
                            #print("inside")
                            if h.bee_inside == False: #if the hole didn't have a bee yet
                                h.bee_inside = True #bee inside true
                                #print("entry")
                                elapsed_time = frame_count / fps #to get the seconds elapsed since beginning                            
                                delta = datetime.timedelta(seconds=elapsed_time)
                                entry_time = start_time + delta
                                print("entry : " + entry_time.strftime("%H:%M:%S"))
                                h.entry_time = entry_time
                            break

                        elif h.bee_inside: #if bee isn't currently in one of the hole but was, we check in the periphery of the hole
                            periphery_hole = Hole("Hoyo Periphery",h.x, h.y, h.radius+15)
                            if periphery_hole.isPointInside(center_x, center_y): #if bee was in a hole and is in periphery, we assume it is getting out
                                #print("exit") 
                                h.bee_inside = False
                                elapsed_time = frame_count / fps #to get the seconds elapsed since beginning                            
                                delta = datetime.timedelta(seconds=elapsed_time)
                                exit_time = start_time + delta

                                duration = (exit_time - h.entry_time).total_seconds() / 60
                                delta = datetime.timedelta(minutes=duration)

                                hours = delta.seconds // 3600
                                minutes = (delta.seconds % 3600) // 60
                                seconds = delta.seconds % 60

                                # Formater la durée en HH:mm:ss
                                duration_formatted = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

                                print([f'Entry : {h.entry_time}', f'Exit : {exit_time}', f'duration: {duration_formatted}', f'Hoyo: {h.name}'])
                                point = (
                                        Point("bees-actions")
                                        .field("entryTime", h.entry_time.strftime("%m/%d/%Y, %H:%M:%S:%f"))
                                        .field("exitTime", exit_time.strftime("%m/%d/%Y, %H:%M:%S:%f"))
                                        .field("holeId", h.name)
                                    )
                                write_api.write(bucket=bucket, org="my-org", record=point)
                                query_api = client.query_api()

                                employee_writer.writerow([f'Entry : {h.entry_time}', f'Exit : {exit_time}', f'duration: {duration_formatted}', f'Hoyo: {h.name}'])
                               
                                # if seconds > 1:
                                #     point = (
                                #         Point("bees-actions")
                                #         .field("entryTime", h.entry_time)
                                #         .field("exitTime", exit_time)
                                #         .field("holeId", h.name)
                                #     )
                                #     write_api.write(bucket=bucket, org="my-org", record=point)
                                #     query_api = client.query_api()

                                    #employee_writer.writerow([f'Entry : {h.entry_time}', f'Exit : {exit_time}', f'duration: {duration_formatted}', f'Hoyo: {h.name}'])
                                h.entry_time = None
                                break

            #Visualizamos el alrededor del área que vamos a análizar
            #Visualizamos el estado de la detección en movimiento
            for hole in holes:
                if hole.bee_inside:
                    cv2.circle(frame, (hole.x, hole.y), hole.radius, (0,0,255), 2)
                else:
                    cv2.circle(frame, (hole.x, hole.y), hole.radius, (0,255,0), 2)
            
            cv2.imshow('frame', frame)

            k = cv2.waitKey(33) & 0xFF
            if k ==27:
                break
    cap.release()
    cv2.destroyAllWindows()