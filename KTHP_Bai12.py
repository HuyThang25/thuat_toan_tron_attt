from Thu_Vien.soNguyenTo import *

n = int(input('Nhập vào n: '))
prime = eratothenes(n)
res = []
for i in range(n+1):
    if prime[i]:
        res.append(i)
for i in range(0, len(res)-4):
    if res[i]+res[i+1]+res[i+2] <= n: 
        if isPrime(res[i]+res[i+1]+res[i+2]):
            print(f'({res[i]},{res[i+1]},{res[i+2]})') 
