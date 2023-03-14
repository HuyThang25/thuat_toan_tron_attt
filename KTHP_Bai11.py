from Thu_Vien.soNguyenTo import *
n = int(input('Nhập vào n:'))
prime = eratothenes(n)
sum=0
for i in range(n+1):
    if prime[i]:
        sum+=i
print(f'Tổng các số nguyên tố nhỏ hơn hoặc bằng {n} = {sum}')