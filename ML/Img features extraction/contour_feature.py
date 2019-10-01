#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html
from __future__ import division
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./images/test.jpg',0)
ret,thresh = cv2.threshold(img,127,255,0)
_,contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)
print (M)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

area = cv2.contourArea(cnt)
perimeter = cv2.arcLength(cnt,True)
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

# hull = cv2.convexHull(points[, hull[, clockwise[, returnPoints]]
k = cv2.isContourConvex(cnt)
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)    

#Rotated Rectangle
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
im = cv2.drawContours(img,[box],0,(135,206,250),2)

#  plt.imshow(im1)
# plt.show()

#Minimum Enclosing Circle
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(0,255,0),2)

# plt.imshow(img)
# plt.show()

#Fitting an Ellipse
ellipse = cv2.fitEllipse(cnt)
im = cv2.ellipse(im,ellipse,(0,255,0),2)

plt.imshow(im)
plt.show()

rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

