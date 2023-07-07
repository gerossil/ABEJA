from ultralytics import YOLO

import numpy as np


model = YOLO('C:\\Users\\LABSIS\\Documents\\ABEJA\\runs\\classify\\train17\\weights\\last.pt')  # load a custom model


results = model('C:\\Users\\LABSIS\\Documents\\ABEJA\\yolo\\Hole_33.png')  # predict on an image



print(results[0].probs)
names_dict = results[0].names
probs = results[0].probs.data
x = list(probs)
print('####################################',x,'####################################')
#print('Catégorie :', names_dict, '| Prob : ', probs)


print(names_dict[np.argmax(x)])