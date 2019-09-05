#bai 1
class diem:
    def __init__(self,pointx=0,pointy=0):
        self.x=pointx
        self.y=pointy
    def nhap(self):
        self.x=int(input("point x: "))
        self.y=int(input("point y: "))
    def xuat(self):
        print("x:",self.x," ; ","y:",self.y)

d=diem()
d.nhap()
d.xuat()