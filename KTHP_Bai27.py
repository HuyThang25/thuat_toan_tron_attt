from Thu_Vien.soNguyenTo import *
from Thu_Vien.euclid import *


prime = eratothenes(999)
for i in range(1,999):
    for j in range(i+1,1000):
        if prime[gcd(i,j)]:
            print(f'({i},{j})',end=' ')



