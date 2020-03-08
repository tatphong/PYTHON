#https://viblo.asia/p/opencv-with-python-part-1-924lJXQaKPM
import cv2
import numpy as np
import matplotlib.pyplot as plt

global img
img = cv2.imread(r'E:\Code\PYTHON\Library_test\img\cat.jpg')
# img = cv2.resize(img,(356,256))
print(img.shape[1],' ',img.shape[0],' ',img.shape[2])
# cv2.imshow('Mèo', img)


def draw_with_plot():
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

    plt.plot([200,00,500],[100,00,100],'c', linewidth=5) 
        #plot():
            # - biến thứ 1 gồm là tọa độ x 3 điểm tạo nên đường thẳng
            # - biến thứ 2 là tọa độ y
            # - biến thứ 3 là màu
    plt.show()


def draw_with_opencv():
    global img
    img=cv2.resize(img,(400,256))
    #tốt nhất nên để resize bên ngoài do ảnh hưởng của biến toàn cục img, cách trên đã giúp giải quyết vấn đề nhưng gây khó hỉu
    cv2.line(img, (200,500), (100,100), (255,0,100), 4)
    cv2.imshow('hello', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

draw_with_plot()
# cv2.imwrite(r'E:\Code\PYTHON\Library_test\img\cat2.png',img) #save image
