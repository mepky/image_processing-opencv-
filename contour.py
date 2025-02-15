import numpy as np 
import cv2

image=cv2.imread("college_id_card.JPEG",1)
gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('Binary',thresh)

_,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image2=image.copy()
index=-1
thichness=4
color=(255,0,255)

cv2.drawContours(image2,contours,index,color,thichness)
cv2.imshow('Contours',image2)


cv2.waitKey(0)
cv2.destroyAllWindows()