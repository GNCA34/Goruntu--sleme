
import cv2
import numpy as np

resim=cv2.imread("joker.jpg")

resim[50,30]=[255,255,255]#bu noktayı beyaza boyadı


for i in range(100):
    resim[70,i]=[255,255,255]##çizgi çektirdik.aşağı 70 sağa 100 e kadar
    
    
cv2.imshow("Joker",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()