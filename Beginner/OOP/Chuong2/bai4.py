class hocsinh:
    def __init__(self,masv=None,ho=None,ten=None,lop=None,d1=0,d2=0,d3=0):      #hàm thiết lập
        self.masv=masv
        self.ho=ho
        self.ten=ten
        self.lop=lop
        self.d1=d1
        self.d2=d2
        self.d3=d3
    def nhap(self):
        self.masv=input("ma sv: ")
        self.ho=input("ho: ")
        self.ten=input("ten: ")
        self.lop=input("lop: ")
        self.d1=int(input("diem 1: "))
        self.d2=int(input("diem 2: "))
        self.d3=int(input("diem 3: "))
    def xuat(self):
        print("masv:",self.masv)
        print("ho ten:",self.ho,self.ten)
        print("lop:",self.lop)
        print("diem 1:",self.d1)
        print("diem 2:",self.d2)
        print("diem 3:",self.d3)
    def dtb(self):
        return (self.d1+self.d2+self.d3)/3
    def xeploai(self):
        dtb=self.dtb()
        if dtb>8:
            return "Gioi"
        elif dtb>6.5:
            return "Kha"
        elif dtb>5:
            return "Trung Binh"
        else:
            return "Kem"

hs=hocsinh()
hs.nhap()
hs.xuat()
print("DTB:",hs.dtb())
print("Xep loai:",hs.xeploai())