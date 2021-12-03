import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('Simul1.PNG',0)
rows,cols = img.shape
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 10)
print(erosion)

M = np.float32([[1,0.25,100],[0.5,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(123)

# global thresholding
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),5)
ret3,th3 = cv2.threshold(blur,0,144,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

plt.plot(th1)
plt.imshow(th1)
plt.show()
cv2.waitKey(123)
