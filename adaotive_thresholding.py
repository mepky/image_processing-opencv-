import numpy as np 
import cv2

image=cv2.imread("college_id_card.JPEG",0)
cv2.imshow('Original ',image)

ret,thres_basic=cv2.threshold (image,70,255,cv2.THRESH_BINARY)
cv2.imshow('Basic Binary',thres_basic)
thres_adapt=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('Adaptive Threshold',thres_adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()