import cv2
import numpy as np
import csv
import datetime
from typing import List
from Hole import Hole
from ultralytics import YOLO

def procesarVideo(holes: List[Hole], peripherical_holes: List[Hole], video):
    global cap, fgbg, kernel
    
    cap = cv2.VideoCapture(video)
    model = YOLO('C:\\Users\\DEPTEC\\Documents\\abejas\\ABEJA\\photo_detection_bees\\runs\\detect\\train2\\weights\\best.pt')  # load a pretrained model

    fgbg = cv2.createBackgroundSubtractorMOG2()
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = 0 #we need to count every frame to get the real time of entries and exits
    start_time = datetime.datetime.now()

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
                                if seconds > 1:
                                    employee_writer.writerow([f'Entry : {h.entry_time}', f'Exit : {exit_time}', f'duration: {duration_formatted}', f'Hoyo: {h.name}'])
                                h.entry_time = None
                                break

            #Visualizamos el alrededor del área que vamos a análizar
            #Visualizamos el estado de la detección en movimiento
            for hole in holes:
                if hole.bee_inside:
                    cv2.circle(frame, (hole.x, hole.y), hole.radius, (0,0,255), 2)
                else:
                    cv2.circle(frame, (hole.x, hole.y), hole.radius, (0,255,0), 2)
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # #dibujamos un rectángulo en frame, para señalar el estado
            # #del área en análisis (movimiento detectado o no detectado)
            # cv2.rectangle(frame, (0,0), (frame.shape[1],40), (0,0,0), -1)
            # color = (0, 255, 0)
            # texto_estado = "Estado: No se ha detectado Abeja"

            # #Con ayuda de una imagen auxiliar, determinamos el area
            # # sobre la cual actuará el detector de movimiento


            # imAux = np.zeros(shape=(frame.shape[:2]), dtype=np.uint8)
            # for hole in peripherical_holes: #Draw the the peripherical area of the hole
            #     imAux = cv2.circle(imAux, (hole.x, hole.y), hole.radius, (255), -1)
            
          
            # image_area = cv2.bitwise_and(gray, gray, mask=imAux)
            # #Obtendremos la imagen binaria donde la región en blanco representa
            # # la existencia de movimiento
            # fgmask = fgbg.apply(image_area)
            # fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
            # fgmask = cv2.dilate(fgmask, None, iterations=2)

            # # Encontramos los contornos presentes de fgmask, para luego basándonos
            # # en su area poder determinar si existe movimiento

            # cnts = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

            # for cnt in cnts:
            #     if cv2.contourArea(cnt) > 100: #if something is detected in the area
            #         x, y, w, h = cv2.boundingRect(cnt)
            #         cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            #         texto_estado = "Estado: Alerta Abeja detectada!!"
            #         color = (0, 0, 255)

            #         # Punto medio del cuadro
            #         middle_point_x = x+w/2
            #         middle_point_y = y+h/2

                    
            #         # Verificar en qué hoyo se encuentra el punto medio
            #         for i, h in enumerate(holes):
            #             if h.isPointInside(middle_point_x, middle_point_y):#if bee is inside one of the hole
            #                 #print("inside")
            #                 if h.bee_inside == False: #if the hole didn't have a bee yet
            #                     h.bee_inside = True #bee inside true
            #                     #print("entry")
            #                     h.entry_time = datetime.datetime.now()
            #                 break

            #             elif h.bee_inside: #if bee isn't currently in one of the hole but was, we check in the periphery of the hole
            #                 periphery_hole = Hole("Hoyo Periphery",h.x, h.y, h.radius+15)
            #                 if periphery_hole.isPointInside(middle_point_x, middle_point_y): #if bee was in a hole and is in periphery, we assume it is getting out
            #                     #print("exit") 
            #                     h.bee_inside = False
            #                     exit_time = datetime.datetime.now()
            #                     duration = (exit_time - h.entry_time).total_seconds() / 60
            #                     delta = datetime.timedelta(minutes=duration)

            #                     hours = delta.seconds // 3600
            #                     minutes = (delta.seconds % 3600) // 60
            #                     seconds = delta.seconds % 60

            #                     # Formater la durée en HH:mm:ss
            #                     duration_formatted = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

            #                     print([f'Entry : {h.entry_time}', f'Exit : {exit_time}', f'duration: {duration_formatted} min', f'Hoyo: {h.name}'])
            #                     employee_writer.writerow([f'Entry : {h.entry_time}', f'Exit : {exit_time}', f'duration: {duration_formatted} min', f'Hoyo: {h.name}'])
            #                     h.entry_time = None
            #                     break

            # #Visualizamos el alrededor del área que vamos a análizar
            # #Visualizamos el estado de la detección en movimiento
            # for hole in holes:
            #     if hole.bee_inside:
            #         cv2.circle(frame, (hole.x, hole.y), hole.radius, (0,0,255), 2)
            #     else:
            #         cv2.circle(frame, (hole.x, hole.y), hole.radius, (0,255,0), 2)


            # cv2.putText(frame, texto_estado, (10,30),
            #             cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

            cv2.imshow('frame', frame)

            k = cv2.waitKey(33) & 0xFF
            if k ==27:
                break
    cap.release()
    cv2.destroyAllWindows()