#https://colab.research.google.com/drive/1Wo3p6VFYqmxY-w52TLbJbsBc9S7p_8LK?fbclid=IwAR0tuwX7XpGyCVpoMGKqg1LqyEVGl4tYx02AFYlE0_fLW6Qf73KlFy08-QE#scrollTo=uUDueT3m9mVn

import tensorflow as tf
## slim là package đi kèm với tensorflow, giúp định nghĩa nhanh các loại mô hình deep learning
import tensorflow.contrib.slim as slim
import tensorflow.contrib.slim.nets
from tensorflow.contrib.slim.nets import vgg 
## sklearn là một thư viện rất phổ biến trong ML, chúng ta chỉ sử dụng tran_test_split để chia data thành 2 tập
from sklearn.model_selection import train_test_split
import json
## thư viện tính toán trên matrix
import numpy as np
import cv2
# thư viện hiển thị biểu đồ
import matplotlib.pyplot as plt
import time

def load():
    labels = json.load(open('train/labels.json'))
    # số lương ảnh
    N = len(labels)
    # matrix chứa ảnh
    X = np.zeros((N, img_size, img_size, 3), dtype='uint8')
    # matrix chứa nhãn của ảnh tương ứng
    y = np.zeros((N,cell_size, cell_size, 5+nclass))
    for idx, label in enumerate(labels):
        img = cv2.imread("train/{}.png".format(idx))
        # normalize về khoảng [0-1]
        X[idx] = img
        for box in label['boxes']:
            x1, y1 = box['x1'], box['y1']
            x2, y2 = box['x2'], box['y2']
            # one-hot vector của nhãn object
            cl = [0]*len(classes)
            cl[classes[box['class']]] = 1
            # tâm của boundary box
            x_center, y_center, w, h = (x1+x2)/2.0, (y1+y2)/2.0, x2-x1, y2-y1
            # index của object trên ma trận ô vuông 7x7
            x_idx, y_idx = int(x_center/img_size*cell_size), int(y_center/img_size*cell_size)
            # gán nhãn vào matrix 
            y[idx, y_idx, x_idx] = 1, x_center, y_center, w, h, *cl
    
    return X, y