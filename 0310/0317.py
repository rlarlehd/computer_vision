import cv2
import matplotlib.pyplot as plt
#Lena 이미지를 컬러영상으로 읽고 화면에 출력하시오.
img = cv2.imread('lena.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()

#영상을 흑백으로 변환하고 화면에 출력하시오
img = cv2.imread('lena.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img_rgb, cmap='gray')
plt.show()
#흑백으로 변환된 영상에 Histogram Equalization을 적용하고 출력하시오.
img=cv2.imread('lena.png')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_hist_eq=cv2.equalizeHist(img_gray)
plt.imshow(img_hist_eq, cmap='gray')
plt.show()
#흑백으로 변환된 영상에 Gamma Correction을 적용하고 출력하시오
img=cv2.imread('lena.png')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gamma=2.0
img_gamma_corrected = cv2.pow(img_gray / 255.0, gamma) * 255.0
img_gamma_corrected = img_gamma_corrected.astype('uint8')
plt.imshow(img_gamma_corrected, cmap='gray')
plt.show()
#영상을 HSV 컬러 스페이스로 변환하고 각각을 화면에 출력하시오. (각값을 0부터 255로 정규화)
img = cv2.imread('lena.png')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img_hsv)
h_norm = cv2.normalize(h, None, 0, 255, cv2.NORM_MINMAX)
s_norm = cv2.normalize(s, None, 0, 255, cv2.NORM_MINMAX)
v_norm = cv2.normalize(v, None, 0, 255, cv2.NORM_MINMAX)
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.imshow(h_norm)
plt.title('Hue')
plt.subplot(1, 3, 2)
plt.imshow(s_norm)
plt.title('Saturation')
plt.subplot(1, 3, 3)
plt.imshow(v_norm)
plt.title('Value')
plt.show()
#H 채널에 대해서 Median Filter를 적용하고 출력하시오.
h_median = cv2.medianBlur(h, 5)
plt.imshow(h_median)
plt.title('H Median')
plt.show()
#S 채널에 대해서 Median Filter를 적용하고 출력하시오.
s_median = cv2.medianBlur(s, 5)
plt.imshow(s_median)
plt.title('S Median')
plt.show()
#V 채널에 대해서 Median Filter를 적용하고 출력하시오.
v_median = cv2.medianBlur(v, 5)
plt.imshow(v_median)
plt.title('V Median')
plt.show()