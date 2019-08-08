import numpy as np 
import cv2

image=cv2.imread("college_id_card.JPEG",1)
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
res,thresh=cv2.threshold(hsv[:,:,0],25,255,cv2.THRESH_BINARY_INV)
cv2.imshow('Thresh',thresh)

edges=cv2.Canny(image,100,70)
cv2.imshow('Canny',edges)

cv2.waitKey(0)
cv2.destroyAllWindows()