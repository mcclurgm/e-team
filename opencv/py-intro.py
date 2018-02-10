import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)
# options: IMREAD_COLOR (0), IMREAD_UNCHANGED (-1), IMREAD_GRAYSCALE (1)

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.plot([50,100], [80,100], "c", linewidth=5)
plt.show()
cv2.imwrite("output.jpg", img)
