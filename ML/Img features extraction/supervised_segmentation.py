# https://towardsdatascience.com/image-segmentation-using-pythons-scikit-image-module-533a61ecc980
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import skimage.data as data
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color

image = io.imread('./images/demo1.png') 
plt.imshow(image)
plt.show()
image_gray = color.rgb2gray(image) 
# image_show(image_gray)
plt.imshow(image_gray)
plt.show()