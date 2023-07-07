from ultralytics import YOLO

model = YOLO('C:\\Users\\LABSIS\\Documents\\ABEJA\\photo_detection\\yolov8m.pt')  # load a pretrained model (recommended for training)

model.train(data='C:\\Users\\LABSIS\\Documents\\ABEJA\\photo_detection\\data_custom.yaml', epochs=20, imgsz=256)
