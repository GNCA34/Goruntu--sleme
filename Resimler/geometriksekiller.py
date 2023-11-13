import cv2 
img=cv2.imread("zeytin.png")
##img=cv2.imread("Resimler/zeytin.png",0) 0 resmi gri yapar
##cv2.imwrite("Zeytingri.png",img)##bir resmi kaydetmek için kullanılır.
cv2.line(img,(0,0),(300,200),(100,100,100),4)##resim üzerine çizgi çizdirme
cv2.rectangle(img,(10,10),(40,40),(255,100,0),3)
cv2.circle(img,(50,100),15,(100,200,100),3)
cv2.ellipse(img,(100,100),(100,200),0,0,360,(0,100,255),3)
cv2.putText(img,'OPENCV',(30,30),cv2.FONT_HERSHEY_SIMPLEX,1,(40,40,40),3,cv2.LINE_AA,False)

cv2.imshow("Zeytin Resmi",img)



cv2.waitKey(0)
cv2.destroyAllWindows()