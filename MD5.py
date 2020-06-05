import math
import struct
from bitarray import bitarray
import hashlib

# Khởi tạo biến:
h0 = 0x67452301
h1 = 0xEFCDAB89
h2 = 0x98BADCFE
h3 = 0x10325476

# Tiền xử lý:
# s="The quick brown fox jumps over the lazy dog"
s = input("Chuỗi cần mã hóa:")
bit_array = bitarray(endian="big")
bit_array.frombytes(s.encode('utf-8'))
    # độn thêm 1 và 000 cho đủ 448 bit
bit_array.append(1)
while bit_array.length() % 512 != 448:
    bit_array.append(0)
    # thêm 1 đoạn 64bit thể hiện chiều dài s vào sau dãy bit
length = (len(s) * 8) % pow(2, 64)
length_bit_array = bitarray(endian="little")
length_bit_array.frombytes(struct.pack("<Q", length))

result = bitarray(bit_array, endian="little").copy()
result.extend(length_bit_array)
# print(result)

    # chặt theo cụm 512 bit
bit_array_len = len(result)
chunk_num = bit_array_len//512

# khai báo các hàm cần thiết
modular_add = lambda a, b: (a + b) % pow(2, 32)
rotate_left = lambda x, n: (x << n) | (x >> (32 - n))
def f(index,b,c,d): # all params is int
    if 0<=index<=15:
        return (b & c) | (~(b) & d)
    if 16<=index<=31:
        return (d & b) | (~(d) & c)
    if 32<=index<=47:
        return b ^ c ^ d
    if 48<=index<=63:
        return c ^ (b | ~(d))

# xác định số dịch chuyển mỗi vòng
r= [7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
    5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
    4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
    6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]

# Sử dụng phần nguyên nhị phân của sin của số nguyên làm hằng số:
k = []
for i in range(64):
    k.append( math.floor((2**32) * abs(math.sin(i + 1))) )

#giải
for i in range(chunk_num):
    # chunk_begin = i*512
    # chunk_end = (i+1)*512-1
    # ngắt chunk thành 16 đoạn con 32bit rồi nhân lên thành 64 đoạn
    w = []*64
    for j in range(0, 64):
        if j<16:
            chunk_begin = i*512 + j*32
            # chunk_end = (i+1)*512-1 + (j+1)*32-1
            w.append(result[chunk_begin:chunk_begin+32])
        else:
            w.append(w[j-16])
    # Convert the `bitarray` objects to integers.
    w = [int.from_bytes(word.tobytes(), byteorder="little") for word in w]
    # solve
    a, b, c, d = h0, h1, h2, h3
    # print(hex(b+int(leftrotate(bin(a + f(0,b,c,d) + k[i] + int(w[i],2)).split('0b')[1], r[i]),2)))
    for i in range(64):
        if 0 <= i <= 15 :
            g = i
        elif 16 <= i <= 31:
            g = (5*i + 1) % 16
        elif 32 <= i <= 47:
            g = (3*i + 5) % 16
        elif 48 <= i <= 63:
            g = (7*i) % 16
        temp = f(i,b,c,d)
        temp = modular_add(temp, a)
        temp = modular_add(temp, w[g])
        # print(temp)
        temp = modular_add(temp, k[i])
        temp = rotate_left(temp, r[i])
        temp = modular_add(temp, b)
        a = d
        d = c
        c = b
        b = temp
        # print(a,b,c,d)
    h0 = modular_add(h0, a)
    h1 = modular_add(h1, b)
    h2 = modular_add(h2, c)
    h3 = modular_add(h3, d)
    # print(h0,h1,h2,h3)

# chuyển 1 chuỗi int thành byte rồi quay về int
A = struct.unpack("<I", struct.pack(">I", h0))[0]
B = struct.unpack("<I", struct.pack(">I", h1))[0]
C = struct.unpack("<I", struct.pack(">I", h2))[0]
D = struct.unpack("<I", struct.pack(">I", h3))[0]

print("actual:", f"{format(A, '08x')}{format(B, '08x')}{format(C, '08x')}{format(D, '08x')}")
print("expected: ",hashlib.md5(s.encode("utf-8")).hexdigest())