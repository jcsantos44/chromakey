import cv2
import numpy as np
from matplotlib import pyplot as plt

#cv2.imshow('asd', th2)
#cv2.waitKey(0)
#cv2.imshow('asd', cv2.erode(th, np.ones((7,7), np.uint8)))
#cv2.waitKey(0)

for i in range(0, 8):
    imgName = str(i) + '.bmp'
    img = cv2.imread(imgName, 0)

    img = cv2.medianBlur(img,5)
    ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

    blur = cv2.GaussianBlur(img,(5,5),0)
    ret3,th2 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                               cv2.THRESH_BINARY,11,2)

    titles = ['Original Image', 'Global Thresholding (v = 127)',
              'Otsu`s thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th1, th2, th3]
    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
        plt.suptitle(imgName)
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()
# cv2.waitKey(0)
