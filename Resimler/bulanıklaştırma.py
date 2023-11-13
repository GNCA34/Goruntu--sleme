import cv2
import numpy as np
img=cv2.imread("zeytin.png")

##kernel=np.ones((3,3),np.float32)/9
##blur=cv2.filter2D(img,-1,kernel)#bulanıklaştırma işlemi
##print(kernel)
"""hazır fonksiyonla bulanıklaştırma"""
blur=cv2.blur(img,(10,10))
cv2.imshow("bulanik zeytin resmi",blur)
cv2.imshow("Zeytin Resmi",img)

cv2.waitKey(0)
cv2.destroyAllWindows()


