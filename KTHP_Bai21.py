from Thu_Vien.soNguyenTo import *

a = int(input('Nhập vào A: '))
b = int(input('Nhập vào B: '))

prime = eratothenes(b)

count = 0
for i in range(a):
    if prime[i]:
        count+=1

for i in range(a,b+1):
    if prime[count]:
        print(i,end=' ')
    if prime[i]:
        count+=1
