import numpy as np 
import cv2

color=cv2.imread("college_id_card.JPEG",1)
gray=cv2.cvtColor(color,cv2.COLOR_RGB2GRAY)
cv2.imwrite('gray.JPEG',gray)
# cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
# cv2.imshow("Image",img)

# cv2.waitKey(0)
# cv2.imewrite('output.JPEG',img)

b=color[:,:,0]
g=color[:,:,1]
r=color[:,:,2]

rgba=cv2.merge((b,g,r,g))
cv2.imwrite('rgba.JPEG',rgba)