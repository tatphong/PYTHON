from Chuong2_bai1 import diem
class DiemMau(diem):
    def __init__(self,x=0,y=0,mau=None):
        super().__init__(x,y)
        self.mau=mau
    def nhap(self):
        super().nhap()
        self.mau=input("Nhap mau: ")
    def xuat(self):
        super().xuat()
        print("Mau",self.mau)

a=DiemMau()
a.nhap()
a.xuat()