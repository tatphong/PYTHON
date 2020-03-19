#https://colab.research.google.com/drive/1Wo3p6VFYqmxY-w52TLbJbsBc9S7p_8LK?fbclid=IwAR0tuwX7XpGyCVpoMGKqg1LqyEVGl4tYx02AFYlE0_fLW6Qf73KlFy08-QE#scrollTo=uUDueT3m9mVn

import tensorflow as tf #tf version==1.15.2
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

#***********************************************************************************************************

# kích thước grid system 
cell_size = 7 
# số boundary box cần dự đoán mỗi ô vuông
box_per_cell = 2
# kích thước ảnh đầu vào
img_size = 224
# số loại nhãn
classes = {'circle':0, 'triangle':1,  'rectangle':2}
nclass = len(classes)

box_scale = 5.0
noobject_scale = 0.5
batch_size = 128
# số lần huấn luyện
epochs = 10
# learning của chúng ta
lr = 1e-3

#**********************************************************************************************************

def load():
    labels = json.load(open(r'D:\Code\PYTHON\ML\YOLO\train\labels.json'))
    # số lương ảnh
    N = len(labels)
    # matrix chứa ảnh
    X = np.zeros((N, img_size, img_size, 3), dtype='uint8')
    # matrix chứa nhãn của ảnh tương ứng
    y = np.zeros((N,cell_size, cell_size, 5+nclass))
    for idx, label in enumerate(labels):
        img = cv2.imread(r"D:\Code\PYTHON\ML\YOLO\train\{}.png".format(idx))
        # normalize về khoảng [0-1]
        X[idx] = img
        for box in label['boxes']:
            x1, y1 = box['x1'], box['y1']
            x2, y2 = box['x2'], box['y2']
            # one-hot vector của nhãn object
            cl = [0]*len(classes)
            cl[classes[box['class']]] = 1
            # tâm của boundary box và chiều dài/rộng của box
            x_center, y_center, w, h = (x1+x2)/2.0, (y1+y2)/2.0, x2-x1, y2-y1
            # index của object trên ma trận ô vuông 7x7
            x_idx, y_idx = int(x_center/img_size*cell_size), int(y_center/img_size*cell_size)
            # gán nhãn vào matrix 
            y[idx, y_idx, x_idx] = 1, x_center, y_center, w, h, *cl
    
    return X, y

#********************************************************************************************************

X, y = load()
#tách X,y thành 2 mảng con là train và test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2018) 
# print (len(X_train),len(X_test))

#********************************************************************************************************

def vgg16(inputs, is_training):
    """định nghĩa CNN
    Args:
      inputs: 5-D tensor [batch_size, width, height, 3]
    Return:
      iou: 4-D tensor [batch_size, 7, 7, 5*nbox + nclass]
    """
    # khái báo scope để có thê group những biến liên quan cho việc visualize trên tensorboard.
    with tf.variable_scope("vgg_16"):
        with slim.arg_scope(vgg.vgg_arg_scope()):
            # hàm repeat có tác dụng lặp lại tầng conv2d n lần mà không phải định nghĩa phức tạp. thank for slim package
            net = slim.repeat(inputs, 2, slim.conv2d, 16, [3, 3], scope='conv1')
            net = slim.max_pool2d(net, [2, 2], scope='pool1')
            net = slim.repeat(net, 2, slim.conv2d, 32, [3, 3], scope='conv2')
            net = slim.max_pool2d(net, [2, 2], scope='pool2')
            net = slim.repeat(net, 2, slim.conv2d, 64, [3, 3], scope='conv3')
            net = slim.max_pool2d(net, [2, 2], scope='pool3')
            net = slim.repeat(net, 2, slim.conv2d, 128, [3, 3], scope='conv4')
            net = slim.max_pool2d(net, [2, 2], scope='pool4')
            net = slim.repeat(net, 2, slim.conv2d, 256, [3, 3], scope='conv5')
            net = slim.max_pool2d(net, [2, 2], scope='pool5')
            
            # thay vì sử dụng 2 tầng fully connected tại đây, 
            # chúng ta sử dụng conv với kernel_size = (1,1) có tác dụng giống hệt tầng fully conntected
            net = slim.conv2d(net, 512, [1, 1], scope='fc6')   

            net = slim.conv2d(net, 13, [1, 1], activation_fn=None, scope='fc7')
    return net

#*****************************************************************************************************************

