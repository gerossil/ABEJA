# ABEJA

    pip install simple_image_download==0.4   

## CONDA 

    !Pour activer L´environnement de Yolo
    conda activate yolov8_custom  


    !Pour installer les dependances
    pip install labelIMG   

    !Pour desactiver Conda 
    conda deactivate yolov8_custom  



### TRAINING YOLO 



    labelIMG "C:\Users\LABSIS\Documents\ABEJA\photo_detection - copia\train\images" "C:\Users\LABSIS\Documents\ABEJA\photo_detection - copia\train\labels\classes.txt"

    Premier Argument : Chemin vers les images d'entrainement 
    Deuxieme Arguement : Chemin vers les classes à charger pour une cohérences des données sinon les labels ont des risques de dériver.

    yolo task=detect mode=train epochs=20 data=data_custom.yaml model="C:\Users\LABSIS\Documents\ABEJA\photo_detection - copia\runs\detect\train5\weights\best.pt" imgsz=640   