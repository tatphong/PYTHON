class hcn:
    def __init__(self,dai=0,rong=0):
        self.dai=dai
        self.rong=rong
    def nhap(self):
        self.dai=int(input("dai: "))
        self.rong=int(input("rong: "))
    def xuat(self):
        print("dai:",self.dai," ; ","rong:",self.rong)
    def dientich(self):
        return self.dai*self.rong
    def chuvi(self):
        return (self.dai+self.rong)*2

a=hcn()
a.nhap()
a.xuat()
print("Dien tich:",a.dientich())
print("Chu vi:",a.chuvi())