import cv2
import numpy as np
kurt=cv2.imread("kurt.jpg")

print(kurt[(230,80)])
print("Resmin boyutu: "+str(kurt.size))
print("Resmin özellikleri: "+str(kurt.shape))
print("Resmin veri tipi:"+str(kurt.dtype))
cv2.imshow("Kurt resmi:",kurt)
cv2.waitKey(0)
cv2.destroyAllWindows()

