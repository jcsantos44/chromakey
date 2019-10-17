import cv2
import numpy as np
from matplotlib import pyplot as plt

bg = cv2.imread('sesto.jpg').astype(np.float32)/255
bgb,bgg,bgr = cv2.split(bg)

for i in range(3, 8):
    imgName = str(i) + '.bmp'
    img = cv2.imread(imgName).astype(np.float32)/255
    img2 = cv2.imread(imgName, 0).astype (np.float32)/255

    b,g,r = cv2.split(img)
    img2 = g - b - r
    img2[img2 < 0] = 0
    
    """cv2.imshow(imgName, np.asarray(img2))
    cv2.waitKey()
    cv2.destroyAllWindows()
    break"""

    for m in range(0, len(img)):
        for n in range(0,len(img[m])):
            gaux = img2[m][n]
            if(gaux > 0.3 and gaux < 0.7):
                raux = (1 - gaux) * r[m][n] + gaux * bgr[m][n]
                baux = (1 - gaux) * b[m][n] + gaux * bgb[m][n]
                gaux = (1 - gaux) * g[m][n] + gaux * bgg[m][n]
                img[m][n] = [baux, gaux, raux]
            if(gaux >= 0.7):
                img[m][n] = bg[m][n]
            

    cv2.imshow(imgName, np.asarray(img))
    cv2.waitKey()
    cv2.destroyAllWindows()
    print('loading next')
