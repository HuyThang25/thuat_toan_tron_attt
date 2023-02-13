import random

def power(x, y, p):
    res = 1;
    x = x % p;
    while (y > 0):
        if (y & 1):
            res = (res * x) % p;
        y = y>>1; # y = y/2
        x = (x * x) % p;
    return res;

def miillerTest(d, n):
    #Chọn một số ngẫu nhiên trong khoảng [2..n-2]
    #Các trường hợp đảm bảo n > 4
    a = 2 + random.randint(1, n - 4);
    # Thực hiện phép tính a^d % n
    x = power(a, d, n);
    if (x == 1 or x == n - 1):
        return True;

    #Tiếp tục bình phương x trong khi một trong các trường hợp sau không xảy ra
    # (i) d không tới n-1
    # (ii) (x^2) % n không bằng 1
    # (iii) (x^2) % n không bằng n-1
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;
        if (x == 1):
            return False;
        if (x == n - 1):
            return True;
    return False;

#Trả về False nếu n là số composite và trả về true nếu n là số nguyên
#K là một tham số đầu vào quyết định mức độ chính xác
#Giá trị k càng cao nghĩa là độ chính xác càng cao

def isPrime( n, k):
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;

    # Tìm giá trị r sao cho n =
    # 2^d * r + 1 với r >= 1
    d = n - 1;
    while (d % 2 == 0):
        d //= 2;

    #Lặp qua k lần
    for i in range(k):
        if (miillerTest(d, n) == False):
            return False;
    return True;

#Số lần lặp
k = 4;
n = int(input())
for i in range(1,n):
    if (isPrime(i, k)):
        print(i , end=" ");