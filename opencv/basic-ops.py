import numpy as np
import cv2

img = cv2.imread("watch.jpg", cv2.IMREAD_COLOR)

# reference a pixel
px = img[55,55]
print(px)

img[55,55] = [0,0,0]

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ROI: region of image
img[100:150, 100:150] = [0,0,0]
roi = img[200:300, 200:300]
snip = roi
img[0:100, 0:100] = snip

cv2.imshow('roi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
