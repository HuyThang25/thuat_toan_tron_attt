from Thu_Vien.soNguyenTo import *

n = int(input('Nhập vào n: '))
print(f'Các số T-Prime nhỏ hơn hoặc bằng {n}: ')
prime = eratothenes(int(math.sqrt(n)))
for i in range(len(prime)):
    if prime[i]:
        print(i*i,end=' ')