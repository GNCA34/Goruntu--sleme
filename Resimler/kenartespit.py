import cv2
import numpy as np
img=cv2.imread("zeytin.png")
canny=cv2.Canny(img,10,200)



cv2.imshow("Zeytin Resmi",img)
cv2.imshow("Kenar tespit",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()


