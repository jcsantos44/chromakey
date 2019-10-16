import cv2
import numpy as np
from matplotlib import pyplot as plt

#cv2.imshow('asd', th2)
#cv2.waitKey(0)
#cv2.imshow('asd', cv2.erode(th, np.ones((7,7), np.uint8)))
#cv2.waitKey(0)

for i in range(0, 8):
    imgName = str(i) + '.bmp'
    img = cv2.imread(imgName, 1)
    """img2 = cv2.imread(imgName)#.astype(np.float32)/255
    img3 = cv2.imread(imgName, 0)#.astype (np.float32)/255
    b,g,r = cv2.split(img2)
    img3 = g - b - r
    img3[img3 < 0] = 0"""

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_green = (42,50,50)
    higher_green = (78,255,255)

    mask = cv2.inRange(hsv,(lower_green),(higher_green), 0.5)

    maskedbgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    #convertidodevoltanovamente = cv2.cvtColor(img3, cv2.COLOR_GRAY2BGR)

    #masked = cv2.subtract(img, convertidodevoltanovamente)

    blurredImage = cv2.GaussianBlur(img,(11,11),0)

    edges = cv2.Canny(blurredImage,100,200)

    blurredEdges = cv2.GaussianBlur(edges,(11,11),0)

    edgesMasked = cv2.subtract (mask, blurredEdges)

    result = cv2.cvtColor(edgesMasked, cv2.COLOR_GRAY2BGR)

    result = cv2.subtract(img,result)

    cv2.imshow("Result", result)
    cv2.waitKey()
