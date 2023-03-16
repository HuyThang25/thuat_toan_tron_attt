from Thu_Vien.soNguyenTo import *

n = int(input('Nhập vào n: '))
prime = eratothenes(n)
res = []
for i in range(n+1):
    if prime[i]:
        res.append(i)
for i in range(0, len(res)-1):
    for j in range(i+1,len(res)):
        if isPrime(res[i]+res[j]) and isPrime(res[j]-res[i]):
            print(f'{res[i]},{res[j]}')
