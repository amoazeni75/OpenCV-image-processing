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






# exit
cv2.waitKey(0)
cv2.destroyAllWindows()
