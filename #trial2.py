#Displaying difference between two images(i.e. moving objects only)
import cv2
cam= cv2.VideoCapture(0)
while cam.isOpened():
    ret,frame1 = cam.read() #first image
    ret,frame2 = cam.read() #second image
    diff = cv2.absdiff(frame1,frame2)#Subtracting images
    grey = cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY) #converting into greyscale
    
    if cv2.waitKey(1)==ord('q'): # 'q' to stop the camera.
        break
    cv2.imshow('My Cam',grey)
 
