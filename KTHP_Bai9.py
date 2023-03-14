from Thu_Vien.soNguyenTo import *
n = int(input('Nhập vào n:'))
prime = eratothenes(n)
count=0
for i in range(n+1):
    if prime[i]:
        count+=1
print(f'Số các số nguyên tố nhỏ hơn hoặc bằng {n} = {count}')