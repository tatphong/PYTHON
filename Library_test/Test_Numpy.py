import numpy as np

def np_arr():
    a = np.array([1, 2, 3])   # Tạo một numpy array với rank = 1
    print(type(a))            # Sẽ in ra "<class 'numpy.ndarray'>"
    print(a.shape)            # Sẽ in ra "(3,)"
    print()

    b = np.array([[1,2,3],[4,5,6]])    # Tạo một numpy array với rank =2
    print(b.shape)                     # In ra "(2, 3)"
    print(b[0, 0], b[0, 1], b[1, 0])   # Sẽ in ra "1 2 4"
    b[0,0]=7
    print(b)
    print()

def np_arr_create():
    a = np.zeros((2,2))   # Tạo một numpy array với tất cả phẩn tử là 0
    print(a)              # "[[ 0.  0.]
                        #   [ 0.  0.]]"
    print()

    b = np.ones((1,2))    # Tạo một numpy array với tất cả phẩn tử là 1
    print(b)              # "[[ 1.  1.]]"

    print()

    c = np.full((2,2), 7)  # Tạo một mảng hằng
    print(c)               # "[[ 7.  7.]
                        #   [ 7.  7.]]"
    print()

    d = np.eye(2)         # Tạo một ma trận đơn vị 2 x 2
    print(d)              # "[[ 1.  0.]
                        #   [ 0.  1.]]"
    print()

    e = np.random.random((2,2))  # Tạo một mảng với các giá trị ngẫu nhiên
    print(e)                     # Có thể là "[[ 0.91940167  0.08143941]
                                #             [ 0.68744134  0.87236687]]"

    print()

    f = np.arange(10) # Tạo 1 numpy array với các phẩn tử từ 0 đến 9
    print(f)          # "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"

    #ép kiểu mảng
    g = np.array([1, 2], dtype = np.float64)

    #tạo mảng cấp số cộng
    np.arange(3)         #array([0, 1, 2])
    np.arange(3, 6)      #array([3, 4, 5])
    np.arange(0, 1, 0.1) #array([ 0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9])

def np_arr_index():
    # Khởi tạo numpy array có shape = (3, 4) có giá trị như sau:
    # [[ 1  2  3  4]
    #  [ 5  6  7  8]
    #  [ 9 10 11 12]]
    a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
    print(a)
    # Sử dụng slicing để tạo numpy array b bằng cách lấy 2 hàng đầu tiên
    # và cột 1, 2. Như vậy b sẽ có shape = (2, 2):
    # [[2 3]
    #  [6 7]]
    b = a[0:2, 1:3]
    print(b)
    # Một array tạo ra từ slicing sẽ có cùng địa chỉ với array gốc.
    # Nếu thay đổi 1 trong 2 thì array còn lại cũng thay đổi.
    print(a[0, 1])   # Prints "2"
    b[0, 0] = 77     # b[0, 0] ở đây tương đương với a[0, 1]
    print(a[0, 1])   # Prints "77"
    print()

def np_arr_index_v2():
    # Tạo một numpy array có shape (3, 4) với giá trị như sau:
    # [[ 1  2  3  4]
    #  [ 5  6  7  8]
    #  [ 9 10 11 12]]
    a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
    
    # Hai cách truy cập dữ liệu ở hàng giữa của mảng
    # Dùng kết hợp chỉ số và slice -> được array mới có rank thấp hơn,
    # Nếu chỉ dùng slice ta sẽ có 1 array mới có cùng rank với array gốc
    row_r1 = a[1, :]    # Rank 1, hàng thứ 2 của a
    row_r2 = a[1:2, :]  # Rank 2, vẫn là hàng thứ 2 của a
    print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
    print(row_r2, row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"
    
    # Chúng ta có thể làm tương tự với cột của numpy array:
    col_r1 = a[:, 1]
    col_r2 = a[:, 1:2]
    print(col_r1, col_r1.shape)  # Prints "[ 2  6 10] (3,)"
    print(col_r2, col_r2.shape)  # Prints "[[ 2]
                                #          [ 6]
                                #          [10]] (3, 1)"



