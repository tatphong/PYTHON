class nguoi:
    def __init__(self,ten=None):
        self.ten=ten
    def nhap(self):
        self.ten=input("Ten: ")
    def xuat(self):
        print(self.ten,"la nguoi")

class hocsinh(nguoi):
    def __init__(self,masv=None,ten=None,lop=None):
        super().__init__(ten)
        self.masv=masv
        self.lop=lop
    def nhap(self):
        super().nhap()
        self.masv=input("Ma sv: ")
        self.lop=input("Lop: ")
    def xuat():
        print(self.ten,"la hoc sinh lop",self.lop,"va masv la",self.masv)

a=hocsinh()
a.nhap()
a.xuat()