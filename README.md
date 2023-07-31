# ABEJA

## REQUIREMENT 

    Application : GIT, Python, Anaconda

### CONFIGURATION 

#### GIT 

    git config --global user.email "leo.gerossier38@gmail.com"
    git config --global user.name "Leo Gerossier"


#### Python sans environnement virtuelle 

    pip install simple_image_download==0.4   




#### CONDA 

    !Création de l´environnement CONDA pour le training de Yolo : 
    conda create -n  yolov8_custom python=3.9

    !Pour activer L´environnement de Yolo
    conda activate yolov8_custom  


    !Pour installer les dependances
    pip install ultralytics
    pip install labelIMG  


    !Pour desactiver Conda 
    conda deactivate yolov8_custom  




##### TRAINING YOLO  

    Explication LabelImage 

    Premier Argument : Chemin vers les images d'entrainement 
    Deuxieme Arguement : Chemin vers les classes à charger pour une cohérences des données sinon les labels ont des risques de dériver.
    Troisième argument : Chemin d'enregistrement des fichiers labels de chaque image

    !Label d'image pour les trous vides/finis et les hotels 
    labelIMG "C:\Users\UMFRAB\Documents\ABEJA\photo_detection\train\images" "C:\Users\UMFRAB\Documents\ABEJA\photo_detection\train\labels\classes.txt" "C:\Users\UMFRAB\Documents\ABEJA\photo_detection\train\labels"
    
    !Label d'image pour les abeilles 
    labelIMG "C:\Users\UMFRAB\Documents\ABEJA\photo_detection_bees\train\images" "C:\Users\UMFRAB\Documents\ABEJA\photo_detection_bees\train\labels\classes.txt" "C:\Users\UMFRAB\Documents\ABEJA\photo_detection_bees\train\labels"
    
    

    !Yolo training pour les trous vides/finis et les hotels
    cd C:\Users\UMFRAB\Documents\ABEJA\photo_detection
    yolo task=detect mode=train epochs=20 data="C:\Users\UMFRAB\Documents\ABEJA\photo_detection\data_custom.yaml" model="C:\Users\UMFRAB\Documents\ABEJA\photo_detection\runs\detect\train8\weights\best.pt" imgsz=640   


    !Yolo training pour les abeilles 
    cd C:\Users\UMFRAB\Documents\ABEJA\photo_detection_bees
    yolo task=detect  mode=train epochs=100 data="C:\Users\UMFRAB\Documents\ABEJA\photo_detection_bees\data_custom.yaml" model="C:\Users\UMFRAB\Documents\ABEJA\photo_detection_bees\runs\detect\train8\weights\best.pt"  imgsz=640   


    !Yolo resume a training of bees
    cd C:\Users\UMFRAB\Documents\ABEJA\photo_detection_bees
    yolo task=detect mode=train resume data="C:\Users\UMFRAB\Documents\ABEJA\photo_detection_bees\data_custom.yaml" model="C:\Users\UMFRAB\Documents\ABEJA\photo_detection_bees\runs\detect\train9\weights\last.pt"  imgsz=640 

    yolo task=detect mode=train resume data="/root/ABEJA/photo_detection_bees/data_custom_linux.yaml" model="/root/ABEJA/photo_detection_bees/runs/detect/train9/weights/last.pt"  imgsz=640 
