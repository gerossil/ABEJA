from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np

# Load the model
model = YOLO('C:\\Users\\LABSIS\\Documents\\ABEJA\\photo_detection - copia\\runs\\detect\\train9\\weights\\best.pt')  # load a pretrained model

# Perform inference

image_path = 'C:\\Users\\LABSIS\\Documents\\ABEJA\\photo_detection - copia\\train\\images\\Hole_31.jpg'


results = model(image_path)

res_plotted = results[0].plot()

resized_image = cv2.resize(res_plotted, (800, 600))  # Adjust the dimensions as needed


cv2.imshow("result", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Load the image
image = Image.open(image_path)

# Create a figure and axes
fig, ax = plt.subplots()

# Display the image
ax.imshow(image)

# Get the bounding boxes and class labels
boxes = results[0].boxes.xyxy.tolist()

#boxes_proba = results[0].boxes.labels

#print("####################", boxes)

labels = results[0].names[0] # Nom des labels names[i] i= valeur du label

#print(boxes_proba)




# Plot the bounding boxes
for box in boxes:
    x_min, y_min, x_max, y_max = box
    
    # Add a rectangle patch
    rect = plt.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min, fill=False, edgecolor='r', linewidth=2)
    
    ax.add_patch(rect)
    # Add the label above the rectangle
    #ax.text(x, y, bbox=dict(facecolor='r', alpha=0.5))

# Show the plot
plt.show()