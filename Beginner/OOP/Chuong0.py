import math
def b1():
    a=int(input("a: "))
    b=int(input("b: "))
    print("tong:",a+b)
    print("hieu:",a-b)
    print("tich:",a*b)
    print("thuong:",a/b)

def b2():
    dai=int(input("chieu dai: "))
    rong=int(input("chieu rong: "))
    print("chu vi:",(dai+rong)*2)
    print("dien tich:",dai*rong)

def b3():
    bankinh=int(input("ban kinh: "))
    print("chu vi:",bankinh*2*math.pi)
    print("dientich:",bankinh*bankinh*math.pi)

def ktchan(n):
    if n%2==0:
        return True
    else:
        return False
def b4():
    n4=int(input("n ktra chan/le: "))
    if ktchan(n4):
        print(n4,"chan")
    else:
        print(n4,"le")

def b5():
    n5=int(input("n ktra am/duong: "))
    if n5>0:
        print(n5,"duong")
    elif n5<0:
        print(n5,"am")
    else:
        print(n5,"la zero") 

snt=[True]*1000001
def sangnt():
    snt[0]=False
    snt[1]=False
    for x in range(2,int(1000000**(0.5))):
        if snt[x]:
            k=x*x
            while k<=1000000:
                snt[k]=False
                k+=x
def b6():
    sangnt()
    n6=int(input("n ktra nguyen to: "))
    if snt[n6]:
        print(n6,"la so nguyen to")
    else:
        print(n6,"ko la so nguyen to")

def b7():
    n7=int(input("n bai 7: "))
    s=0
    chan=0
    le=0
    sngto=0
    sangnt()
    for i in range(0,n7+1):
        s+=i
        if ktchan(i):
            chan+=1
        else:
            le+=1
        if snt[i]:
            sngto+=1
    print ("tong:",s)
    print ("chan:",chan)
    print ("le:",le)
    print ("snt:",sngto)
    print (n7,"so ngto dau tien la:")
    for j in range(0,1000000):
        if snt[j]:
            print(j)
            n7-=1
        if n7<=0:
            break

def duyet(arr):
    print(arr)
def b8():
    n8=int(input("n bai 8: "))
    arr=[]
    for i in range(0,n8):
        arr.append(int(input("nhap: ")))
    duyet(arr)
    them=int(input("Them phan tu: "))
    arr.append(them)
    xoa=int(input("xoa phan tu thu: "))
    del arr[xoa]
    duyet(arr)
    x=int(input("x can tim: "))
    if x in arr:
        for i in range(len(arr)):
            if arr[i]==x:
                print("vi tri x la:",i)
                break

def b9():
    s=input("chuoi: ")
    s=s.strip()
    s=s.replace("  "," ")
    print (s)
    print(len(s))
    for i in range(len(s)):
        print(s[i])
    k=int(input("nhap k: "))
    print(k,"ky tu ben trai:",s[0:k])
    print(k,"ky tu ben phai:",s[len(s)-k:len(s)])
    n=int(input("nhap n: "))
    print(k,"den",k+n,":",s[k:k+n])
    
b9()