import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
#50
d = 100
start_coordinate= (200, 200)

for i in range(0,5):
    for j in range(0,5):
        #d = 50
        d_i = d*i
        d_j = d*j
        center_coordinate = (200+d_i, 200+d_j)
    


#def drawcircle(center_coordinate):

        whiteblankimage = np.zeros(shape=[1024, 1024,3], dtype=np.uint8)
        cv.circle(whiteblankimage, center=center_coordinate, radius=100, color=(10,0,0), thickness=-1)
        whiteblankimage = cv.cvtColor(whiteblankimage, cv.COLOR_BGR2GRAY )
        os.chdir("C:/Users/JaianthV/switchdrive3/Ptychography_paper/python/overlap_images/")
        cv.imwrite("image_%d_%d.tiff"%(i,j),whiteblankimage)


#def save_image(image):


#def plot(image):
plt.imshow(whiteblankimage)

plt.show()
