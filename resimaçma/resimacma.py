
import cv2
import numpy as np

resim=cv2.imread("logo.png",0)##resim aynı ama siyah beyaza dönüşür.Gri

cv2.imshow("Logo resmi",resim)

cv2.imwrite("grilogo.png",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()##opencv yle alakalı tüm pencereler kapanıyor

