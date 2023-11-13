import cv2
import numpy as np
img=cv2.imread("zeytin.png")

kernel=np.array([[-1,-1,-1],
                [-1,9,-1],
                [-1,-1,-1]])
keskinlestirme=cv2.filter2D(img,-1,kernel)

cv2.imshow("Zeytin Resmi",img)
cv2.imshow("Keskinlestirilmis zeytin resmi",keskinlestirme)

cv2.waitKey(0)
cv2.destroyAllWindows()


