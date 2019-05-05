<h1>AI_image_proccessing</h1>

<p>This project introduces some applied functions in image processing that written with python and opencv library.</p>

<p> first step you must install python3, you can download python setup according to your operation system from here :</p>
<p>https://www.python.org/downloads/</p>
<p>for windows you need to add path of python packages to your enviroment variables, follow these steps:</p>
<ol type="1">
  <li>search "edit the system enviroment variables"</li>
  <li>click on "Enviroment Variables..." button</li>
  <li>in the user section, select "Path" then click on "Edit" button</li>
  <li>in the oppened window click "New" then enter this path according to your username and installed python version</li>
      <o1 type="2">
        <li> C:\Users\"username here for example : Alireza"\AppData\Local\Programs\Python\"Python + version for example : Python36-   32"\Scripts\</li>
  <li> C:\Users\"username here for example : Alireza"\AppData\Local\Programs\Python\"Python + version for example : Python36-           32"\</li></o1>
  <li>click ok and then Apply</li> 
 </o1>
 
<p>next you need to install opencv, for windows follow these steps:</p>
<o1 type  = "1">
  <li>press windows key + R</li>
  <li>type "cmd"</li>
  <li>copy and paste this line and then press enter: <code>pip install opencv-python</code></li>
  <li>then enter this command : <code>pip install opencv-contrib-python --upgrade</code></li>
 </o1>
 <p1>to ensure that all things is ok, type these lines in cmd, then you should see the version of your installed opencv :<p>
  <code>C:\> python</code>
  <code>import cv2</code>
  <code>print(cv2.__version__)</code>
    
<p>after setuping pre-requirments you can run cmd and go to directory of .py downloaded file and type : <code>python P2_9423110.py</code></p>
<p>note : you should put an image with the name "test.jpg" in the directory of P2_9423110.py file</p>

<h1>here is the list of functions that this script contains</h1> 
<ul>
  <li>open and show test.jpg picture as normal image</li>
  <li>show blue channel of openned image</li>
  <li>convert the image to grayscale one and show it</li>
  <li>smooth the gray scale image with Gaussian filter and then show it</li>
  <li>rotate the input image 90 degree and show it</li>
  <li>change width of the image without changing it's height</li>
  <li>detect edges and show them</li>
  <li>segement the input image and then show it</li>
  <li>reconize faces in the image and draw rectangle around each of them</li>
</ul>
