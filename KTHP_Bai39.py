from Thu_Vien.soNguyenTo import *
from Thu_Vien.euclid import *

n = int(input('Nhập vào số phần tử mảng: '))
print('Nhập vào mảng: ')
arr=[int(input()) for i in range(n)]
max=arr[0]
for i in range(1,n):
    if max<arr[i]: max = arr[i]
prime = eratothenes(max)

for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if prime[gcd(arr[i],arr[j])]:
            print(f'({arr[i]},{arr[j]})',end=' ')

