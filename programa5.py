import cv2
import numpy as up

scala_reference = 20.0 
reference_width = None
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break 

    gray = cv2