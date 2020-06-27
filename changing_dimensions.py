import cv2
import numpy as np
import os

files=os.listdir('JPEGImages/')
for i,file in enumerate(files):
    if(i%500==0):
        print(f"{i} images processed successfully.")
    img=cv2.imread('JPEGImages/'+file,1)
    shape=img.shape
    upper_pad=max((512-shape[0])//2,0)
    lower_pad=max((512-shape[0]-upper_pad),0)
    left_pad=max((512-shape[1])//2,0)
    right_pad=max((512-shape[1]-left_pad),0)
    img = np.pad(img,((upper_pad,lower_pad),(left_pad,right_pad),(0,0)),mode='edge')
    cv2.imwrite('Images/'+file,img)

