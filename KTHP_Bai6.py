import math
def isF_number(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum+=i
    return sum == n
n = int(input('Nhập vào n: '))
print(f'Các số F-number nhỏ hơn {n}: ')
for i in range(2,n+1):
    if (isF_number(i)):
        print(i,end=' ')
        
    