import cv2
from time import sleep
# AI_Project 2
# S.Alireza Moazeni
# 9423110   Amirkabir university of technology
# Fall 2018


# 1 Loads image as such including alpha channel and then show it again
import numpy as np

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
cv2.imshow('Resize image section 6', resize)

# 7 edge detection with canny function
edge = cv2.Canny(img1, 100, 200)
cv2.imshow('Edges in image section 7', edge)

# 8 segmentation
img_segment = cv2.imread('test.jpg')
ret, thresh = cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)
# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1
# Now, mark the region of unknown with zero
markers[unknown==255] = 0
markers = cv2.watershed(img_segment,markers)
img_segment[markers == -1] = [255,0,0]
cv2.imshow('Segmentation section 8', img_segment)


#9 face detection
face_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_eye.xml')

img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv2.imshow('Face Detection', img)

#10 extract 5 frame with delay 0.5 second between each oder
video_frame = []
vidcap = cv2.VideoCapture("test.avi")
for i in range(5):
    success, image = vidcap.read()
    cv2.imshow('Frames with intervals of 0.5 seconds -' + repr(i + 1), image)
    cv2.waitKey(500)

# show 5 first frame with delay 0.5 second
for i in range(5):
    success, image = vidcap.read()
    video_frame.append(image)

for i in range(5):
    cv2.imshow('First 5 frame -' + repr(i + 1), video_frame[i])
    cv2.waitKey(500)

# exit
cv2.waitKey(0)
cv2.destroyAllWindows()
