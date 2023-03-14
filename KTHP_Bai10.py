from Thu_Vien.soNguyenTo import *
n = int(input('Nhập vào n: '))
k,s=0,0
for i in range(1,n+1):
    if n%i==0: 
        s+=1
        if isPrime(i):
            k+=1
print(f'{n} có {s} ước số và {k} ước nguyên tố')