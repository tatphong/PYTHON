# from __future__ import print_function
import numpy as np 
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
np.random.seed(22)

means = [[2, 2], [4, 2]]
cov = [[.3, .2], [.2, .3]]
N = 15
X0 = np.random.multivariate_normal(means[0], cov, N) # class 1print(X0)
X1 = np.random.multivariate_normal(means[1], cov, N) # class -1 
X = np.concatenate((X0.T, X1.T), axis = 1) # all data 
# print(X)
y = np.concatenate((np.ones((1, N)), -1*np.ones((1, N))), axis = 1) # labels 


#tìm nghiệm
from sklearn.svm import SVC

y1 = y.reshape((2*N,))
# print(y1)
X3 = X.T # each sample is one row
# print(X1)
clf = SVC(kernel = 'linear', C = 1,probability=True) # just a big number 

clf.fit(X3, y1) 
print(clf)
w = clf.coef_
b = clf.intercept_
print('w = ', w)
print('b = ', b)
print(clf.support_)
# plt.scatter(X1[:,0],X1[:,1])
x1 = np.arange(1.5, 4, 0.2)
y1 = -w[0, 0]/w[0, 1]*x1 - b/w[0, 1]
y2 = -w[0, 0]/w[0, 1]*x1 - (b-1)/w[0, 1]
y3 = -w[0, 0]/w[0, 1]*x1 - (b+1)/w[0, 1]
plt.plot(x1, y1, 'k', linewidth = 3)
plt.plot(x1, y2, 'k')
plt.plot(x1, y3, 'k')
plt.plot(X0[:, 0], X0[:, 1], 'bs', markersize = 6, alpha = .8)
plt.plot(X1[:, 0], X1[:, 1], 'ro', markersize = 6, alpha = .8)
# plt.plot(clf.n_support_,'r')
plt.show()
# print(1e5)