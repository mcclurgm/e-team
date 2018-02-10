import numpy as np
import cv2

img1 = cv2.imread("img1.png", cv2.IMREAD_COLOR)
img2 = cv2.imread("img2.png", cv2.IMREAD_COLOR)
watch = cv2.imread("watch.jpg", cv2.IMREAD_COLOR)

cv2.imshow('roi', watch)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.imshow('roi', img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# basic arithmetic
add = cv2.add(img1, img2) # can img1+img2 technically, but weird. don't.
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
# img1, weight of 1, img2, weight of 2, gamma
# weights add to 1

# logical operations: eg add watch without white bg
rows, cols, channels = watch.shape # get dimensions of watch (channels unused)
roi = img1[0:rows, 0:cols]
watchgray = cv2.cvtColor(watch, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(watchgray, 253, 255, cv2.THRESH_BINARY_INV)
# img, boundary, if < convert to this (otherwise black apparently), type
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
watch_fg = cv2.bitwise_and(watch, watch, mask=mask)
dst = cv2.add(img1_bg, watch_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('roi', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
