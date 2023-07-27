

from ultralytics.yolo.data.annotator import auto_annotate

auto_annotate(data="C:\\Users\\LABSIS\\Documents\\ABEJA\\Yolo_Segmentation\\Hole_33.png", det_model="yolov8x.pt", sam_model='sam_b.pt')