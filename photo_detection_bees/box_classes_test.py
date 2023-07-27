import torch
from pathlib import Path
from PIL import Image
import yaml
import os 


def load_model(model_path):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    
    model = model.to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
    model.eval()
    return model

def detect_objects(model, img_path, conf_threshold=0.5, iou_threshold=0.5):
    img = Image.open(img_path)
    results = model(img)


    return results.pred[0]

def save_labels(img_path, detections, output_dir):
    if detections.numel() == 0:
        print("No detections found.")
        return

    if detections.dim() == 2:
        for detection in detections:
            img_width, img_height = Image.open(img_path).size

            output_file = Path(output_dir) / Path(img_path).name.replace('.jpg', '.txt')


            with open(output_file, 'w') as f:
                for detection in detections:
                    print(detection)
                    class_idx, x_center, y_center, width, height = detection[0][:5]

                    # Convert coordinates to YOLO format (normalized)
                    x_center /= img_width
                    y_center /= img_height
                    width /= img_width
                    height /= img_height

                    line = f'{int(class_idx)} {x_center} {y_center} {width} {height}\n'
                    f.write(line)
    else:
        print("Invalid detections tensor format.")    

    

if __name__ == '__main__':
    model_path = 'C:\\Users\\UMFRAB\\Documents\\ABEJA\\photo_detection_bees\\runs\\detect\\train8\\weights\\best.pt'  # Replace with the path to the YOLOv5 model checkpoint
    
    path_dossier = 'C:\\Users\\UMFRAB\\Documents\\ABEJA\\photo_detection_bees\\bees_v2'  # Replace with the path to your image
    
    output_directory = 'C:\\Users\\UMFRAB\\Documents\\ABEJA\\photo_detection_bees\\train\\labels'  # Replace with the directory where you want to save the label files
    model = load_model(model_path)

    for nom_fichier in os.listdir(path_dossier):
        if nom_fichier.endswith(".jpg") or nom_fichier.endswith(".png") or nom_fichier.endswith(".jpeg"):

            image_path = os.path.join(path_dossier, nom_fichier)
    
    
            
            detections = detect_objects(model, image_path)

            if detections[0] is not None:
                save_labels(image_path, detections, output_directory)
            else:
                print("No objects detected.")
