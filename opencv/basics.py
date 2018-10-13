#!/usr/bin/python
import numpy as np
import cv2

# Load image
img = cv2.imread('sample-image.jpg', 0)
# syntax: imread('filename', image_read_method)
# method: cv2.{IMREAD_COLOR (-1), IMREAD_GRAYSCALE (0), IMREAD_UNCHANGED (1)}

# Display image
cv2.imshow('Sample Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.imshow('window-name', image_variable)
# waitKey: wait until a key is pressed
# destroyAllWindows: destroy any of the windows we created

# Videos
# Video capture
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Run operations on the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display result
    cv2.imshow('A grayscale frame', gray)
    # Wait for 'q' key to end run
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Clean up at end
cap.release()
cv2.destroyAllWindows()
