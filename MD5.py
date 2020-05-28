import math
import hashlib
# xác định số dịch chuyển mỗi vòng
r=[7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
    5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
    4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
    6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]

# Sử dụng phần nguyên nhị phân của sin của số nguyên làm hằng số:
k = []
for i in range(0,63):
    k.append( math.floor((2**32) * abs(math.sin(i + 1))) )

# Khởi tạo biến:
h0 = 0x67452301
h1 = 0xEFCDAB89     #these are int
h2 = 0x98BADCFE
h3 = 0x10325476

# Tiền xử lý:
# s="The quick brown fox jumps over the lazy dog"
s = input("Chuỗi cần mã hóa:")
s = s.encode('utf-8')
s_hex = s.hex()
s_bin = bin(int(s_hex, 16)).split('0b')[1]
    # chặt theo 512 bit
s_bin_len = len(s_bin)
chunk_num = s_bin_len//512+1
    # độn thêm 1000 cho đủ 448 bit
s_bin+="1"
while len(s_bin) < chunk_num * 512 - 64:
    s_bin+="0"
    # độn 0000 phía trước bit cho đủ 64 bit
s_bin_len = bin(s_bin_len).split('0b')[1]
while len(s_bin_len) < 64:
    s_bin_len = '0'+s_bin_len
    # kết hợp lại đủ bội số 512 bit
s_bin += s_bin_len

def modular_add(a,b):
    return (a+b)%pow(2,32)

def leftrotate(x, c): # x:int, c:int
    x=bin(x<<c).split("0b")[1]
    if len(x)>32:
        a=x[:-32]
        x=x[-32:]
        x=x[:-len(a)]
        x+=a
    return int(x,2)
rotate_left = lambda x, n: (x << n) | (x >> (32 - n))

def f(index,b,c,d): # all params is int
    if 0<=index<=15:
        return (b and c) or (not(b) and d)
    if 16<=index<=31:
        return (d and b) or (not(d) and c)
    if 32<=index<=48:
        return b ^ c ^ d
    if 49<=index<=63:
        return c ^ (b or not(d))
    
for i in range(chunk_num):
    # chunk_begin = i*512
    # chunk_end = (i+1)*512-1
    # ngắt chunk thành 16 đoạn con 32bit
    w = []*64
    for j in range(0, 64):
        if j<16:
            chunk_begin = i*512 + j*32
            # chunk_end = (i+1)*512-1 + (j+1)*32-1
            w.append(s_bin[chunk_begin:chunk_begin+31])
        else:
            w.append(w[j-16])

    # solve
    a, b, c, d = h0, h1, h2, h3
    # print(hex(b+int(leftrotate(bin(a + f(0,b,c,d) + k[i] + int(w[i],2)).split('0b')[1], r[i]),2)))
    for i in range(0, 63):
        temp = f(i,b,c,d)
        temp = modular_add(temp, a)
        temp = modular_add(temp, int(w[i],2))
        temp = modular_add(temp, k[i])
        print("temp: "+str(bin(temp)))
        temp = rotate_left(temp, r[i])
        temp = modular_add(temp, b)
        a = d
        d = c
        c = b
        b = temp
        # print(str(i)+" / "+hex(b))
    
    h0 = modular_add(h0, a)
    h1 = modular_add(h1, b)
    h2 = modular_add(h2, c)
    h3 = modular_add(h3, d)
    print(hex(h0)+" "+hex(h1)+" "+hex(h2)+" "+hex(h3))

print(hex(int( (bin(h0).split('0b')[1] + bin(h1).split('0b')[1] + bin(h2).split('0b')[1] + bin(h3).split('0b')[1]) ,2)).split('0x')[1])
    

# print(s_bin)
# print(w)
print(hashlib.md5(s).hexdigest())