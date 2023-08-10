


# ABEJA

## REQUIREMENT 

    Application : GIT, Python, Anaconda, Docker

### CONFIGURATION 

#### GIT 

    git config --global user.email "leo.gerossier38@gmail.com"
    git config --global user.name "Leo Gerossier"


    pip install simple_image_download==0.4   

## CONDA 

    conda create -n  yolov8_custom python=3.9

    !Pour activer L´environnement de Yolo
    conda activate yolov8_custom  


    !Pour installer les dependances
    pip install labelIMG   

    !Pour desactiver Conda 
    conda deactivate yolov8_custom  



### TRAINING YOLO 



    labelIMG "C:\Users\LABSIS\Documents\ABEJA\photo_detection\train\images" "C:\Users\LABSIS\Documents\ABEJA\photo_detection\train\labels\classes.txt"
    
    

    Premier Argument : Chemin vers les images d'entrainement 
    Deuxieme Arguement : Chemin vers les classes à charger pour une cohérences des données sinon les labels ont des risques de dériver.

    yolo task=detect mode=train epochs=20 data="C:\Users\LABSIS\Documents\ABEJA\photo_detection\data_custom.yaml" model="C:\Users\LABSIS\Documents\ABEJA\photo_detection\runs\detect\train8\weights\best.pt" imgsz=640   



     yolo task=detect mode=train epochs=20 data="C:\Users\LABSIS\Documents\ABEJA\photo_detection_bees\data_custom.yaml"  imgsz=640   



### Run Solution
flask --app app.py run
docker compose up -d
influx setup --name myinfluxdb2 --host http://localhost:8086 \
  -u admin -p admin54321 -o my-org \
  -b my-bucket -t my-token -r 0 -f

Add grafana data source
