#Security Cam 1.0
import cv2
import datetime as dt
cam= cv2.VideoCapture(0)
while cam.isOpened():
    ret,frame1 = cam.read()
    ret,frame2 = cam.read()
    diff = cv2.absdiff(frame1,frame2) #taking difference of both images.
    grey = cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY) #converting into grayscale.
    blur = cv2.GaussianBlur(grey,(5,5),0) #bluring to reduce noise and even up moving surface.
    _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY) #applying threshold to sharpen the images.
    dilated = cv2.dilate(thresh,None,iterations=3) #dilation to join broken parts of object(morphological operation).
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #drawing contours.
    
    for c in contours:
        if cv2.contourArea(c) > 5000: #excluding small contours.
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
            #Saving frame 
            moment=str(dt.datetime.today()).replace(' ','_').replace(':','-') #formating current date and time for filename.
            fname='Intruders//intruder_'+moment+'.jpg' #'Intruders' is the target folder for saving files.
            cv2.imwrite(fname,frame1)
        
        
    if cv2.waitKey(1)==ord('q'):
        break
    cv2.imshow('Security camera 0',frame1)
 
