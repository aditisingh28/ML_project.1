
import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haaarcascade_eye.xml")

#capture frames from camera
cap=cv2.VideoCapture(0)
#loop will run if caputre has been initiated
while 1:
    #read fram from camera
    ret ,img=cap.read()
    #converts to gray scale of each frame 
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    #detect faces of different sizes in the input image
    face= face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        #finding eye within face
        eye = eye_cascade.detectMultiScale(roi_gray)
        #to draw rectangle in face
        for (ex,ey,ew,eh) in eye:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    #dispay image in window
    cv2.imshow('img',img)
    #waiting for esckey to stop
    k = cv2.waitkey(30) & 0xff
    if k ==27:
        break
#close the window
cap.release()   
cv2.destroyAllWindows()