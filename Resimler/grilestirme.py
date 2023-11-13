import cv2
import numpy as np
img=cv2.imread("zeytin.png")
imgGri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Zeytin Resmi",img)
cv2.imshow("Gri Zeytin Resmi",imgGri)

size_y=img.shape[0]##shape[0] yüksekliği ifade eder
size_x=img.shape[1]##shape[1] genişilği ifade eder
kanal=img.shape[2]#kanal sayısı

##resmin 3 özelliği var.Gri resimde kanal sayısı yoktur
print("Yükseklik:",size_y,"Genişlik:",size_x,"Kanal Sayısı:",kanal)
##Gri resimler için kanal sayısı olmadığı için hata verir.
print(img[(121,250)])##renk değerini alır

cv2.waitKey(0)
cv2.destroyAllWindows()


