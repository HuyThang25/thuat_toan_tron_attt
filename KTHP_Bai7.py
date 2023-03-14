import math
def isPrime(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

def reverse_interger(n):
    r = 0
    while n>0:
        r = r*10 + n%10
        n=n//10
    return r

n = int(input('Nhập vào n: '))
print(f'Các số emirp nhỏ hơn {n}: ')
for i in range(2,n+1):
    if isPrime(reverse_interger(i)):
        print(i,end=' ')
