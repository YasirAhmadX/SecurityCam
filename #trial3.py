#Blurring subtrating images and then sharpening then with given threshold.
import cv2
cam= cv2.VideoCapture(0)
while cam.isOpened():
    ret,frame1 = cam.read()
    ret,frame2 = cam.read()
    diff = cv2.absdiff(frame1,frame2)
    grey = cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY) #converting into greyscale
    blur = cv2.GaussianBlur(grey,(5,5),0) #blur to evenup the surfaces and reduce noise
    _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY) #sharpening blur image
    
    if cv2.waitKey(1)==ord('q'):
        break
    cv2.imshow('My Cam',thresh)
 
