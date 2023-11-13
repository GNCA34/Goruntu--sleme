import cv2
import numpy as np



kemalsunal=cv2.imread("indir.jpeg")
"""kemalsunal[:,:,0]=255 #BGR   B:0 G:1 R:2 
#kemalsunal[:,:,1]=80
"""
kemalsunal[50:80,135:210,0]=255# ilk parametre y pixel, ikinci parametre x pixel
cv2.imshow("Kemal Sunal",kemalsunal)


cv2.waitKey(0)#herhangi bir tuşa basaba kadar ekranın açık kalmasını sağlar
cv2.destroyAllWindows()
