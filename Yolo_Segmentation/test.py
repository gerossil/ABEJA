from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt
import cv2


yolo = YOLO()

# Call the predict method with the appropriate arguments

model = YOLO('C:\\Users\\LABSIS\\Documents\\ABEJA\\runs\\classify\\train17\\weights\\last.pt')  # load a custom model

image = Image.open("C:\\Users\\LABSIS\\Documents\\ABEJA\\yolo\\Hole_33.png") 

frame = cv2.imread("C:\\Users\\LABSIS\\Documents\\ABEJA\\yolo\\Hole_33.png")

img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

results = model.predict(img)

print(results)

for r in results:
    for c in r.boxes.cls:
        print(model.names[int(c)])

    cv2.imshow('YOLO V8 Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break



results = model.predict(source='C:\\Users\\LABSIS\\Documents\\ABEJA\\yolo\\train.jpeg')

print(results[0].probs)



plt.figure(figsize=(15, 15))
plt.imshow(image)





def show_box(box, ax):
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0,0,0,0), lw=2))


for result in results:
    print(result.boxes)
    #x = list(result.boxes.xyxy.tolist())
    #print(x)


plt.axis('off')
plt.show()
