# ABEJA

## REQUIREMENT 

You'll need the following applications installed:

* GIT
* Python
* Anaconda
* Docker

### CONFIGURATION 

#### GIT 

Configure your global GIT user email and name:

    git config --global user.email "Mame@provider.com"
    git config --global user.name "Name"


#### Python without virtual environment

Install a specific version of the simple_image_download package:

pip install simple_image_download==0.4

#### CONDA 

Create a Conda environment named "yolov8_custom" with Python 3.9: 
    
    conda create -n  yolov8_custom python=3.9


Activate the "yolov8_custom" Conda environment:

    conda activate yolov8_custom  


Install dependencies using pip:
   
    pip install ultralytics
    pip install labelIMG  


Deactivate the Conda environment:

    conda deactivate yolov8_custom  




##### TRAINING YOLO  

Explanation of LabelImage:

* First Argument: Path to training images
* Second Argument: Path to classes file for data consistency
* Third Argument: Path to save label files for each image

Label images for different classes:

  *  Example for empty/finished holes and hotels
    
    labelIMG "path_to_train_images" "path_to_classes.txt" "path_to_labels_directory"

  *  Example for bees
    
    labelIMG "path_to_train_images" "path_to_classes.txt" "path_to_labels_directory"

# Perform YOLO training for different classes:
  
  *  Example for empty/finished holes and hotels
        
    cd path_to_photo_detection
    yolo task=detect mode=train epochs=20 data="path_to_data_custom.yaml" model="path_to_best.pt" imgsz=640

  *  Example for bees
    
    cd path_to_photo_detection_bees
    yolo task=detect mode=train epochs=20 data="path_to_data_custom.yaml" model="path_to_best.pt" imgsz=640

 *   Resume training

    cd path_to_photo_detection_bees
    yolo task=detect mode=train resume data="path_to_data_custom.yaml" model="path_to_last.pt" imgsz=640

    
  
### Flask Requirement

Install required packages for the Flask application:

    pip install Flask influxdb influxdb_client reportlab moviepy

### Run Solution Flask 

Run the Flask application:

    
    flask --app app.py run --reload

### Run Solution Docker

Run the Docker container using Docker Compose:

   * Setup InfluxDB :

    docker compose up -d
    influx setup --name myinfluxdb2 --host http://localhost:8086 \
    -u admin -p admin54321 -o my-org \
    -b my-bucket -t my-token -r 0 -f

 
Please replace the placeholders like path_to_... with the actual paths and names of your files and directories. Make sure to have the necessary permissions and access to execute these commands.