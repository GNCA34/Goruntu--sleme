import cv2

image=cv2.imread("adisyonbos.jpg",0)
ret,thresh1=cv2.threshold(image,210,255,cv2.THRESH_BINARY)

cv2.imshow("original",image)
cv2.imshow("thresh1",thresh1)

cv2.waitKey(0)
cv2.destroyAllWindows()