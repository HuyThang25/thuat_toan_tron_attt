from Thu_Vien.soNguyenTo import *
from Thu_Vien.euclid import *

a = int(input('Nhập vào a: '))
b = int(input('Nhập vào b: '))

prime = eratothenes(b)
for i in range(a,b):
    for j in range(i+1,b+1):
        if prime[gcd(i,j)]:
            print(f'({i},{j})',end=' ')


