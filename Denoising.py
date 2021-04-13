import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
from skimage.filters import median
from skimage.morphology import disk

Image = cv.imread("star.jpg", 0)

MedianImage = median(Image, disk(3), mode='constant', cval=0)
GaussianImage = cv.GaussianBlur(Image, (3, 3), 0, borderType=cv.BORDER_CONSTANT)
MedianUsingCV = cv.medianBlur(Image, 3)
cv.imshow("OriginalImage", Image)
cv.imshow("MedianCV", MedianUsingCV)
cv.imshow("GaussianImage", GaussianImage)
cv.imshow("MedianImage", MedianImage)


cv.waitKey(0)
cv.destroyAllWindows()
