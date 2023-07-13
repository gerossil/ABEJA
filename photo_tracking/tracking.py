from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load an official detection model


# Track with the model
results = model.track(source="C:\\Users\\LABSIS\\Documents\\ABEJA\\photo_tracking\\video-zoomed.mp4", show=True) 
