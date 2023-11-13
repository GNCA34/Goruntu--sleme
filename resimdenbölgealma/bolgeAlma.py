import cv2
import numpy as np

resim=cv2.imread("indir (1).jpeg")
kesit=resim[100:300,30:200]
kesit[:,:,2]=255##kesilen alanı kırmızıya boyadım.
cv2.imshow("kesit alani",kesit)

cv2.imshow("23 Nisan",resim)


cv2.waitKey(0)
cv2.destroyAllWindows()
