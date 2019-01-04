# ai_image_proccessing
This project introduces some applied functions in image processing that written with python and opencv libs.

#in first step you must install python3, you can download python setup according to your operation system here :
</br>https://www.python.org/downloads/
</br>- for windows you need to add path of python packages to your enviroment variables, follow these steps:
</br> - search "edit the system enviroment variables"
</br>2 - click on "Enviroment Variables..." button
</br>3 - in the user section select "Path" then click on "Edit" button
</br>4 - in the oppened window click "New" then in enter this path according to your username and installed python version
</br>a : C:\Users\"username here for example : Alireza"\AppData\Local\Programs\Python\"Python + version for example : Python36-           #         32"\Scripts\
</br>b : C:\Users\"username here for example : Alireza"\AppData\Local\Programs\Python\"Python + version for example : Python36-           #         32"\
</br>5 - click ok and then Apply 
  
</br>next you need to install opencv, for windows follows this steps:
</br>1 - press windows key + R
</br>2 - type "cmd"
</br>3 - copy paste this line and then press enter: "pip install opencv-python"
</br>4 - then enter this command : "pip install opencv-contrib-python --upgrade"
</br>- to sure that all things is ok, type these line in cmd, then you should see version of your opencv :
</br>C:\> python
</br>>>> import cv2
</br>>>> print(cv2.__version__)
    
</br>after setup pre requirments you can run cmd in the path of .py downloaded file and type : python P2_9423110.py
</br>note : you should place an image with name "test.jpg" in the directory of P2_9423110.py file

</br>functions list in the code : 
</br>1 - open and show test.jpg picture
</br>2 - show blue channel of openned image
</br>3 - convert image to grayscale and show it
</br>4 - smooth gray scale image with Gaussian filter and then show it
</br>5 - rotate input image 90 degree and show it
</br>6 - change width but take height no change
</br>7 - detect edges and show them
</br>8 - segement input image and then show it
</br>9 - reconize faces in image and draw rectangle around each of them
