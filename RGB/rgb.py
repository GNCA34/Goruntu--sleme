import cv2
import numpy as np

resim=cv2.imread("images.jpeg")##resim aynı ama siyah beyaza dönüşür.Gri
cv2.imshow("kus",resim)

print(resim.size)
print(resim.dtype)
print(resim.shape)#genişlik yükseklik kanal


cv2.waitKey(0)
cv2.destroyAllWindows()##opencv yle alakalı tüm pencereler kapanıyor

