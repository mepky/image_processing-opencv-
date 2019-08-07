import numpy as np 
import cv2
image=cv2.imread("college_id_card.JPEG")

#scale
img_half=cv2.resize(image,(0,0),fx=0.5,fy=0.5)
img_stretch=cv2.resize(image,(600,600))
img_stretch_near=cv2.resize(image,(600,600),interpolation=cv2.INTER_NEAREST)

cv2.imshow('Half',img_half)
cv2.imshow('Stretch',img_stretch)
cv2.imshow('Stretch near',img_stretch_near)

#Rotation 
M=cv2.getRotationMatrix2D((0,0),-30,1)
rotated=cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow('Rotated',rotated)


cv2.waitKey(0)
cv2.destroyAllWindows()