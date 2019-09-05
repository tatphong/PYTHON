import matplotlib.pyplot as plt
import numpy as np
def plot_auto_generate_x_value():
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.show()

def plot_format_style():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro') #1 số kiểu định dạng như: ro,bo ; k,r--
    plt.axis([0, 6, 0, 20])
    plt.show()

def plot_sin_cos():
    X = np.linspace(-np.pi, np.pi, 100, endpoint=True)
    #x=np.arange(0.,8.0,0.1)
    C,S = np.cos(X), np.sin(X)
    plt.plot(X, C)
    plt.plot(X,S)
    plt.show()

def plot_tan():
    X = np.linspace(-np.pi, np.pi, 100, endpoint=True)
    t = np.tan(X)
    plt.plot(X, t)
    plt.show()

def plot_ax():
    a,b = int(input("nhap a: ")), int(input("nhap b: "))
    x=np.arange(10)
    plt.plot(a*x+b)
    plt.show()

def plot_ax2():
    a,b,c = int(input("nhap a: ")), int(input("nhap b: ")), int(input("nhap c: "))
    x=np.arange(10)
    plt.plot(a*x**2+b*x+c,'r--')
    plt.show()

def plot_apx_log_ex():
    a=int(input("nhap a: "))
    x=np.arange(3, 10)
    plt.plot(x,a**x,'g')
    plt.show()
    plt.plot(x,np.exp(x),'r')
    plt.show()
    plt.plot(x,np.log(x),'b')
    plt.show()

def plot_gauss():
    x=np.arange(-20,21)
    o=5
    u=0
    plt.title("Phân phối chuẩn (Gauss)")
    plt.plot(x,1/(o*np.sqrt(2*np.pi))*np.exp(-(x-u)**2/(2*o**2)))
    plt.show()

plot_gauss()
