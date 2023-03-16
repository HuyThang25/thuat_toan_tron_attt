from Thu_Vien.soNguyenTo import *

n = int(input('Nhập vào n: '))
k = int(input('Nhập vào k: '))
prime = eratothenes(n)
res = []
for i in range(n+1):
    if prime[i]:
        res.append(i)

for i in range(0, len(res)-k):
    sum=0
    for j in range(k):
        sum+=res[i+j]
    if sum <= n: 
        if prime[sum]:
            print(f'({res[i]}',end='')
            for j in range(1,k):
                print(f',{res[i+j]}',end='')
            print(')')
                
                 
