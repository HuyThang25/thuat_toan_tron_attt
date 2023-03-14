from Thu_Vien.soNguyenTo import *
n = int(input('Nhập vào n:'))
prime = eratothenes(n)
pre = -1
for i in range(3,n+1,2):
    if prime[i]:
        if pre != -1:
            print(f'({pre},{i})')
        pre = i
    else:
        pre = -1
    