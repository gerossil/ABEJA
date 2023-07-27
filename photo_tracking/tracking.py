from ultralytics import YOLO

# Load a model
model = YOLO('C:\\Users\\UMFRAB\\Documents\\ABEJA\\photo_detection_bees\\runs\\detect\\train9\\weights\\best.pt')  # load an official detection model


# Track with the model
results = model.track(source="C:\\Users\\UMFRAB\\Documents\\ABEJA\\photo_tracking\\bees_v4_inside.mp4", conf=0.5, show=True, persist=True) 
