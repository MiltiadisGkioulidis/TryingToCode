import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


image = cv.imread("star.jpg", 0)
median = cv.medianBlur(image, 3)
#plt.hist(image.flat, bins=100, range=(0, 255))
#plt.show()
ret, th = cv.threshold(median, 120, 255, cv.THRESH_TOZERO)
cv.imshow("IMAGE", image)
cv.imshow("DenoisedImage", median)
cv.imshow("ThresholdedImage", th)
cv.waitKey(0)
cv.destroyAllWindows()


