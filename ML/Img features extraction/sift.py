import cv2
import numpy as np
import matplotlib.pyplot as plt

# read image 
img = cv2.imread('./images/demo0.jpg')


# color gray of image
# ey(0)
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# use sift of cv2
sift = cv2.xfeatures2d.SIFT_create(150) # the 50 is around amount of key points
#print(sift.hessianThreshold)

# detect and compute image
#kp = sift.detect(gray,None)
#kp1,des = sift.compute(gray,kp1)
kp, des = sift.detectAndCompute(gray,None)
print(len(kp))
print(len(des))
print(des.shape)
print(type(kp))
print(type(des))
print()
print(kp)
print()
print(des)

#cv2.drawKeypoints(gray,kp,img)
#img = cv2.drawKeypoints(gray,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# cv2.imshow("image",img)
# cv2.waitKey(0)
plt.imshow(img),plt.show()
# ghi file
cv2.imwrite('sift_keypoints.jpg',img)

