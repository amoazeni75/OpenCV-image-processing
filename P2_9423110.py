import cv2
# AI_Project 2
# S.Alireza Moazeni
# 9423110   Amirkabir university of technology
# Fall 2018


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

# 5 rotate input image with 90 degree
rotated = cv2.rotate(img1, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('Rotated image 90 degree section 5', rotated)

# 6 resize image to (w/2 , h)
resize = cv2.resize(img1, (0,0), fx=0.5, fy=1)
cv2.imshow('resize image section 6', resize)

# exit
cv2.waitKey(0)
cv2.destroyAllWindows()
