# I have no idea if this works or not, my webcam doesn't work.
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("frame", frame)
    else:
        break

    if cv2.waitKey(1) & 0xFF == ord("1"):
        break

cap.release()
cv2.destroyAllWindows()
