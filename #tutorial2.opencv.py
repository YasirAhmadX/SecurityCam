import cv2
cam= cv2.VideoCapture(0)
while cam.isOpened():
    ret,frame1 = cam.read()
    ret,frame2 = cam.read()
    diff = cv2.absdiff(frame1,frame2)
    grey = cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY) #converting into greyscale
    
    if cv2.waitKey(1)==ord('q'):
        break
    cv2.imshow('My Cam',grey)
 
