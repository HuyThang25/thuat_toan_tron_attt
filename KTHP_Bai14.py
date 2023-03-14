from Thu_Vien.soNguyenTo import *

def reverse_interger(n):
    r = 0
    while n>0:
        r = r*10 + n%10
        n=n//10
    return r

prime = eratothenes(999)

for i in range(100,1000):
    if prime[reverse_interger(i)]:
        print(i,end=' ')
