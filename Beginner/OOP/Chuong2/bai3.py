import math

class htron:
    def __init__(self,bankinh=0):
        self.r=bankinh
    def nhap(self):
        self.r=int(input("ban kinh: "))
    def xuat(self):
        print("ban kinh:",self.r)
    def dientich(self):
        return self.r**2*math.pi
    def chuvi(self):
        return self.r*2*math.pi

a=htron(10)
a.xuat()
print("Dien tich:",a.dientich())
print("Chu vi:",a.chuvi())