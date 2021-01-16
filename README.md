# SecurityCam
SecurityCam is a motion detection software which uses Python and OpenCV.
## License
  [Licensed  under MIT License](https://github.com/EccentricX/SecurityCam/blob/main/LICENSE)

## Modules Required
### SecurityCam1.0
  Security Cam1.0 uses cv2 and datetime module.**cv2 module** contains necessary function to *access camera , take photos , process the same and finally display them* . **datetime module** provides us date and time info for the moment when movement was detected.
  
  **datetime module** comes with python package , however to cv2 needs to be installed.Type following command on cmd to install cv2 (For Microsoft Windows OS).

    pip install opencv-python
    
 ## Working
 SecurityCam(1.0) captures 2 photos in each iteration and then takes absolute difference of them to detect any change, if camera is stationary then this change signifies motion. The program then processes these images *(morphological operations)* to reduce noise and join broken parts of the object and draws contours around them. It then checks the area of the moving object and if it is more than a particular number(5000 as in 1.0) then is draws a bigger contours around that small contours are ignored. Program then saves those photos (with contours) in folder named 'Intruders' on current working directory. Photos are named under the format
 
    intruder_YYYY-MM-DD_HH-MM-SS.nS
 
 
