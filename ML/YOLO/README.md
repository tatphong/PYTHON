# YOLO
- Objects detection
## Dataset
- 25000 basic geometry images
## Build CNN Model
- YOLO model using vgg16 architcture (5 Conv2D layers, 5 MaxPooling2D layer, 2 Conv2D layer with kennel=(1,1) to place fully connected layer, IOU, Loss, Optimizer: Adam, filter)
- Using linear regression to predict 2 boundary_box in each grid_box
## Getting Started
- Library: tensorflow, sklearn, json, numpy, cv2, matplotlib, time