class sinhvien():
    def __init__(self,array_sv=[]):
        self.array_sv=array_sv
    def nhap(self):
        ss=int(input("So sv can nhap: "))
        for i in range(0,ss):
            self.array_sv.append(input("Nhap sv: "))
    def xuat(self):
        print("Si so:",len(self.array_sv))
        for i in range(len(self.array_sv)):
            print(i+1,self.array_sv[i])
    def xoa(self):
        ten=input("Nhap ten sv muon xoa :")
        for i in range(len(self.array_sv)):
            if self.array_sv[i]==ten:
                del self.array_sv[i]
                break

sv=sinhvien()
sv.nhap()
sv.xuat()
sv.xoa()
sv.xuat()