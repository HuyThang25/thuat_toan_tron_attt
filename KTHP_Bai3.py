from Thu_Vien.soNguyenTo import *
n = int(input('Nhập vào n: '))
k,q,p,s=0,0,0,0
for i in range(1,n+1):
    if n%i==0: 
        p+=i
        s+=1
        if isPrime(i):
            k+=1
            q+=i
print(n+p+s-q-k)