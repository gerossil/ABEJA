from Hole import Hole
import cv2
import numpy as np

from detectar_mov_area4 import procesarVideo

#Carga el video
cap = cv2.VideoCapture("nido.mp4")

#Lee el primer frame
ret, frame = cap.read()
img = frame

coordinates = []
holes = []
counter = 1

def draw_square(event, x, y, flags, param):
    global coordinates, holes, counter

    #Si se presiona el botón izquierdo del mouse, comienza a dibujar el cuadrado
    if event == cv2.EVENT_LBUTTONDOWN:
        start_point = (x, y)
        coordinates.append(start_point)
        #print("Start Point: ", start_point)

    #Si se suelta el botón izquierdo del mouse, detiene el dibujo del cuadrado
    elif event == cv2.EVENT_LBUTTONUP:
        end_point = (x, y)
        coordinates.append(end_point)
        #print("End Point: ", end_point)

        #Si se almacenan 2 puntos, dibuja el cuadrado
        if len(coordinates) == 2:
            cv2.rectangle(img, coordinates[0], coordinates[1], (0, 255, 0), 2)
            cv2.imshow("Image", img)
            x1, y1 = coordinates[0]
            x2, y2 = coordinates[1]
            holes.append(Hole("Hoyo"+str(counter),np.array([[x1,y1],[x1,y2],[x2,y2],[x2,y1]])))
            counter += 1
            #Reinicia las coordenadas
            coordinates = []

#Crea una ventana y establece una función de devolución de llamada del mouse
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", draw_square)

#Muestra el primer frame
cv2.imshow("Image", img)

#Espera a que el usuario presione 'q' para salir
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        for hole in holes:
            print("Name: ", hole.name)
            print("Coordinates: \n", hole.coordinates)
        procesarVideo(holes)
        break

#Libera la captura de video
cap.release()
cv2.destroyAllWindows()


