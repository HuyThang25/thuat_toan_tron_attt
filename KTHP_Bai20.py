from Thu_Vien.euclid import *
m = int(input('Nhập vao m: '))
n = int(input('Nhập vao n: '))
d = int(input('Nhập vao d: '))
for i in range(m+1,n-1):
    for j in range(i+1,n):
        if (gcd(i,j)==d):
            print(f'({i},{j})',end=' ')

