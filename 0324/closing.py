import cv2, math
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./lena.png')

KSIZE = 11
ALPHA = 2
kernel = cv2.getGaussianKernel(KSIZE, 0)
kernel = -ALPHA * kernel @ kernel.T
kernel[KSIZE//2, KSIZE//2] += 1 + ALPHA
print(kernel.shape, kernel.dtype, kernel.sum())

unsharp = cv2.filter2D(image, -1, kernel)
dx = cv2.Sobel(unsharp, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(unsharp, cv2.CV_32F, 0, 1)

kernel = cv2.getGaborKernel((21, 21), 5, 1, 10, 1, 0, cv2.CV_32F)
kernel /= math.sqrt((kernel * kernel).sum())

filtered = cv2.filter2D(unsharp, -1, kernel)

dx_norm = cv2.normalize(cv2.magnitude(dx, dx), None, 0, 1, cv2.NORM_MINMAX, cv2.CV_32F)
filtered_norm = cv2.normalize(filtered.astype(np.float32), None, 0, 1, cv2.NORM_MINMAX, cv2.CV_32F)
diff = cv2.absdiff(dx_norm, filtered_norm)
def on_trackbar(val):
    thresh = val / 100.0
    _, result = cv2.threshold(diff, thresh, 1.0, cv2.THRESH_BINARY)
    kernel_morph = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    closed = cv2.morphologyEx(result, cv2.MORPH_CLOSE, kernel_morph)
    cv2.imshow('Closing Threshold', closed)

cv2.namedWindow('Closing Threshold')
cv2.createTrackbar('x0.01', 'Closing Threshold', 0, 100, on_trackbar)
on_trackbar(0)
cv2.waitKey(0)
cv2.destroyAllWindows()