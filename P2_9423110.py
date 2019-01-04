import img as img
import numpy as np
import cv2


# 1 Loads image as such including alpha channel and then show it again
img1 = cv2.imread('test.jpg', -1)
cv2.imshow('Normal Image section 1', img1)

# 2 show just blue channel of image
blueImg = img1.copy()
blueImg[:, :, 1] = 0
blueImg[:, :, 2] = 0
cv2.imshow('Blue channel section 2', blueImg)

# 3 convert to gray scale
img_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Scale Image section 3', img_gray)

# 4 smooth gray scale image with gaussian filter
gaussian_img = cv2.GaussianBlur(img_gray, (5, 5), 0, 0)   # kernel size 5 * 5
cv2.imshow('Gaussian filter section 4', gaussian_img)

# exit
cv2.waitKey(0)
cv2.destroyAllWindows()
