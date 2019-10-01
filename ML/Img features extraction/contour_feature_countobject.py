# https://datacarpentry.org/image-processing/09-contours/
import cv2, sys
import matplotlib.pyplot as plt

# read command-line arguments
# filename = sys.argv[1]
t = 5 #int(sys.argv[0])

# read original image
image = cv2.imread('./images/Capture.png')

# create binary image
gray = cv2.cvtColor(src = image, code = cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(src = gray, 
    ksize = (5, 5), 
    sigmaX = 0)
(t, binary) = cv2.threshold(src = blur,
    thresh = t, 
    maxval = 255, 
    type = cv2.THRESH_BINARY)

(_, contours, _) = cv2.findContours(image = binary, 
    mode = cv2.RETR_EXTERNAL,
    method = cv2.CHAIN_APPROX_SIMPLE)

print("Found %d objects." % len(contours))
for (i, c) in enumerate(contours):
    print("\tSize of contour %d: %d" % (i, len(c)))

cv2.drawContours(image = image, 
    contours = contours, 
    contourIdx = -1, 
    color = (0, 0, 255), 
    thickness = 5)

plt.imshow(image)
plt.show()