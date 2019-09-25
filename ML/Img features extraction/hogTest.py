import cv2
import numpy as np
import matplotlib.pyplot as plt
# Read image
img = cv2.imread('faces\\running.jpg')
img = np.float32(img) / 255.0
cv2.imshow('image',img)
cv2.waitKey(0)
# Calculate gradient 
gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=1)
print(gx)
gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=1)
# Next, we can find the magnitude and direction of gradient using the 

# Python Calculate gradient magnitude and direction ( in degrees ) 
mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)
# print(mag)
print()
print(mag.shape)
# print(angle)
cv2.imshow('image',mag)
cv2.waitKey(0)
cv2.imshow('image',angle)
cv2.waitKey(0)
# plt.scatter(gx,gy)
# plt.show()