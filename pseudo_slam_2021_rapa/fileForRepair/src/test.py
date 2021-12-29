import cv2
import numpy as np
 
cap = cv2.VideoCapture(0) 
ret,frame = cap.read()
print(ret)
cv2.imshow('img',frame)
cv2.waitKey()
cv2.destroyAllWindows()