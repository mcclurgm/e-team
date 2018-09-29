import numpy as np
import cv2

img = cv2.imread("watch.jpg", cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,150), (255,0,0), 15)
# (img, start, end, color (BGR), linewidth)
cv2.rectangle(img, (15,25), (200,150), (0,255,0), 5)
# (img, start, end, color, linewidth)
# linewidth = -1: fill no stroke
# alse circle

# polygon: points connected
pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,0,255), 5)
# img, points, connect final to first pt?, color, linewidth

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
