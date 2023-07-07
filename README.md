# ABEJA



## CONDA 

    !Pour activer L´environnement de Yolo
    conda activate yolov8_custom  


    !Pour installer les dependances
    pip install labelIMG   

    !Pour desactiver Conda 
    conda deactivate yolov8_custom  



## TRAINING YOLO 



    labelIMG

    yolo task=detect mode=train epochs=100 data=data_custom.yaml model="C:\Users\LABSIS\Documents\ABEJA\photo_detection - copia\runs\detect\train9\weights\best.pt" imgsz=640   