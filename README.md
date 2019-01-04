# ai_image_proccessing
This project introduces some applied functions in image processing that written with python and opencv libs.

#in first step you must install python3, you can download python setup according to your operation system here :
#https://www.python.org/downloads/
#- for windows you need to add path of python packages to your enviroment variables, follow these steps:
#  1 - search "edit the system enviroment variables"
#  2 - click on "Enviroment Variables..." button
#  3 - in the user section select "Path" then click on "Edit" button
#  4 - in the oppened window click "New" then in enter this path according to your username and installed python version
#      a : C:\Users\"username here for example : Alireza"\AppData\Local\Programs\Python\"Python + version for example : Python36-           #         32"\Scripts\
#      b : C:\Users\"username here for example : Alireza"\AppData\Local\Programs\Python\"Python + version for example : Python36-           #         32"\
#  5 - click ok and then Apply 
  
# next you need to install opencv, for windows follows this steps:
#  1 - press windows key + R
#  2 - type "cmd"
#  3 - copy paste this line and then press enter: "pip install opencv-python"
#  4 - then enter this command : "pip install opencv-contrib-python --upgrade"
#- to sure that all things is ok, type these line in cmd, then you should see version of your opencv :
#    C:\> python
#	  >>> import cv2
#	  >>> print(cv2.__version__)
    
# after setup pre requirments you can run cmd in the path of .py downloaded file and type : python P2_9423110.py
#note : you should place an image with name "test.jpg" in the directory of P2_9423110.py file

# functions list in the code : 
#  1 - open and show test.jpg picture
#  2 - show blue channel of openned image
#  3 - convert image to grayscale and show it
#  4 - smooth gray scale image with Gaussian filter and then show it
#  5 - rotate input image 90 degree and show it
#  6 - change width but take height no change
#  7 - detect edges and show them
#  8 - segement input image and then show it
#  9 - reconize faces in image and draw rectangle around each of them
