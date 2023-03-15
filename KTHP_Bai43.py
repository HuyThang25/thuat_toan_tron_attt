import math
import time
import random

random.seed(time.time())

def isPrime(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

def RandomSearch():
    n=random.randint(1,100)
    for i in range(2,100):
        if n == i: continue
        if n % i ==0: return RandomSearch()
    if isPrime(n):
        return n
    return RandomSearch()

# def getRandomBit(k):
#     return random.randint(0,2**k-1)

# def RandomSearch(k,t):
#     n=getRandomBit(k)
#     for i in range(2,100):
#         if n == i: continue
#         if n % i ==0: return RandomSearch(k,t)
#     if isPrimeMillerRabin(n,t):
#         return n
#     return RandomSearch(k,t)
def nhanBinhPhuongLap(a,k,n):
    b=1
    if (k==0):
        return (b)
    A = a
    t = round(math.log2(k))
    if (k%2==1):
        b=a
    k=k>>1
    for i in range(1,t+1):
        A = A**2 % n
        if (k%2==1):
            b = A*b % n
        k=k>>1
    return b
def isPrime(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True
n = int(input('Nhập vào N: '))
p = RandomSearch()

print(f'Số p khi sinh là: {p}')
print('Các số a thoả mãn là:')
for a in range(1,n):
    if isPrime(nhanBinhPhuongLap(a,p,n)):
        print(a,end=' ')


    
