#https://www.kaggle.com/zeemeen/glcm-texture-features
#https://gogul.dev/software/texture-recognition
#https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_glcm.html
#https://stackoverflow.com/questions/35551249/implementing-glcm-texture-feature-with-scikit-image-and-python    this source
import matplotlib.pyplot as plt
import gdal, gdalconst
import numpy as np
from skimage.feature import greycomatrix, greycoprops

filename = "//mnt//glaciology//RS2_20140101.jpg"
outfilename = "//home//max//Documents//GLCM_contrast.tif"
sarfile = gdal.Open(filename, gdalconst.GA_ReadOnly)

sarraster = sarfile.ReadAsArray()
#sarraster is satellite image, testraster will receive texture
testraster = np.copy(sarraster)
testraster[:] = 0

for i in range(testraster.shape[0] ):
    print (i),
    for j in range(testraster.shape[1] ):

        #windows needs to fit completely in image
        if i <3 or j <3:
            continue
        if i > (testraster.shape[0] - 4) or j > (testraster.shape[0] - 4):
            continue

        #Calculate GLCM on a 7x7 window
        glcm_window = sarraster[i-3: i+4, j-3 : j+4]
        glcm = greycomatrix(glcm_window, [1], [0],  symmetric = True, normed = True )

        #Calculate contrast and replace center pixel
        contrast = greycoprops(glcm, 'contrast')
        testraster[i,j]= contrast

sarplot = plt.imshow(testraster, cmap = 'gray')