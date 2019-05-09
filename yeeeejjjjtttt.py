import numpy as np
import serial
import time
import cv2

# Setup for arduino
arduino = serial.Serial('COM3', 9600)
time.sleep(2)
print("Connected to arduino...")
# importing the Haarcascade(Put name for your haar cascade here if your's is named differently)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eyes_defualt.xml')
# To capture the video stream from webcam.
cap = cv2.VideoCapture(0)
count = 0

# Read the image, convert it to GrayScale and find the faces contained within the image
while 1:
    ret, img = cap.read()
    cv2.resizeWindow('img', 500, 500)
    cv2.line(img, (500, 250), (0, 250), (0, 255, 0), 1)
    cv2.line(img, (250, 0), (250, 500), (0, 255, 0), 1)
    cv2.circle(img, (250, 250), 5, (255, 255, 255), -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3)

# detect the face and make a rectangle around it.
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # Center of rectangle
        xx = int(x+(x+h))/2

        j = int(xx)  # because why not
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (100, 0, 155), 2)


            arduino.write(str(j).encode())

# Display video
    cv2.imshow('img', img)

# Hit 'Esc' to terminate execution
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
