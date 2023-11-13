import cv2
import numpy as np

resim=cv2.imread("images.jpeg")
aynalananResim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)
uzatilanResim=cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_REPLICATE)
tekrarlananResim=cv2.copyMakeBorder(resim,300,300,300,300,cv2.BORDER_WRAP)
cerceveResim=cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT,
                                value=(0,0,255))

cv2.imshow("Aynalanan Adile Nasit",aynalananResim)
cv2.imshow("Uzatilan Adile Nasit",uzatilanResim)
cv2.imshow("Tekrarlanan Adile Nasit",tekrarlananResim)
cv2.imshow("Sarılan Adile Nasit",cerceveResim)



cv2.waitKey(0)
cv2.destroyAllWindows()
