#code sử dụng đa hình
class DongVat:
    def __init__(self,ten=None,cannang=None):
        self.ten=ten
        self.cannang=cannang
    def nhap(self):
        self.ten=input("Ten: ")
        self.cannang=input("Can nang: ")
    def xuat(self):
        print(self.ten,"la dong vat ; can nang",self.cannang)
class Meo(DongVat):
    def __init__(self,ten=None,cannang=None,maulong=None):
        super().__init__(ten,cannang)
        self.maulong=maulong
    def nhap(self):
        super().nhap()
        self.maulong=input("Mau long: ")
    def xuat(self):
        print("Con meo",self.ten,"nang",self.cannang,"mau",self.maulong)

n=int(input("Nhap n:"))
arr=[None]*n
for i in range(0,n):
    print("1) Dong vat\n2) Meo")
    chon=int(input("Chon: "))
    if chon==1:
        arr[i]=DongVat()
        arr[i].nhap()
    else:
        arr[i]=Meo()
        arr[i].nhap()
for i in range(0,5):
    arr[i].xuat()