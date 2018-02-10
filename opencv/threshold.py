import numpy as np
import cv2

img = cv2.imread("bookpage.jpg", cv2.IMREAD_COLOR)
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
retval, threshold2 = cv2.threshold(grayscale, 12, 255, cv2.THRESH_BINARY)
# anything brighter than 12 will be white, darker will be black (in color)

# gaussian adaptive threshold
gauss = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                              cv2.THRESH_BINARY, 115, 1)
retval, otsu = cv2.threshold(grayscale, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('img', img)
cv2.imshow('colthresh', threshold)
cv2.imshow('thresh', threshold2)
cv2.imshow('gauss', gauss)
cv2.imshow('otsu', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
