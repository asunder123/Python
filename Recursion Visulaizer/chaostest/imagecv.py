import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('Simul1.PNG',0)


# global thresholding
ret1,th1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)


ret,thresh3= cv2.threshold(img,200,200,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
print("Images",img)
edges = cv2.Canny(th1,2000,2000)
print("Edges",edges)
rows,cols = img.shape
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 10)
print(erosion)
#M = np.float32([[1,0.25,100],[0.5,1,50]])
for i in range(60):
 M = cv2.getRotationMatrix2D((cols/2,rows/2),45,i)
 dst = cv2.warpAffine(thresh3,M,(cols,rows))
 cv2.imshow('img',dst)
 cv2.waitKey(123)

#plt.plot(th1)
#plt.imshow(th1)
print(th1.size)
plt.imshow(dst,cmap = 'gray')
print("Dst Magnified",dst)
plt.show()
cv2.waitKey(123)
