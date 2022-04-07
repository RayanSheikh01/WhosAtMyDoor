import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0) # Num in parantheses stands for which camera, 0 (or -1) is first camera, etc

if not cap.isOpened():
    print("Camera cannot be opened.")
    exit()

while True: 
    # Capture frame by frame
    ret, frame = cap.read()

    # If frame is read correctly, return value is True
    if not ret:
        print("Frame cannot be received. Exiting...")
        break

    # Frame operations below
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

# After everything is done, release capture
cap.release()
cv.destroyAllWindows()