'''
* Created on: feb 12, 2020
 '''

import cv2
import sys
import numpy as npy
i0=cv2.imread("img0.jpg",0)
i1=cv2.imread("img1.jpg",0)
i2=cv2.imread("img2.jpg",0)
i3=cv2.imread("img3.jpg",0)
i4=cv2.imread("img4.jpg",0)
i5=cv2.imread("img5.jpg",0)
i6=cv2.imread("img6.jpg",0)
i7=cv2.imread("img7.jpg",0)
i8=cv2.imread("img8.jpg",0)
i9=cv2.imread("img9.jpg",0)
i10=cv2.imread("img10.jpg",0)

width=npy.size(i0,1)
height = npy.size(i0,0)
newImage = npy.zeros((height, width, 3), dtype=npy.uint8)


for i in range(0,height):
    for j in range(0,width):
        value=[]
        value.append(i0[i,j])
        value.append(i1[i,j])
        value.append(i2[i,j])
        value.append(i3[i,j])
        value.append(i4[i,j])
        value.append(i5[i,j])
        value.append(i6[i,j])
        value.append(i7[i,j])
        value.append(i8[i,j])
        value.append(i9[i,j])
        value.append(i10[i,j])
        value.sort()
        
        newImage[i,j]=value[int(len(value))//2+1]

cv2.imshow('output',newImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

