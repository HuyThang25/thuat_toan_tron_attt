from Thu_Vien.soNguyenTo import *
from math import *

n = int(input('Nhập vào n: '))

prime = eratothenes(int(sqrt(n)))

res = []
for i in range(len(prime)):
    if prime[i]:
        res.append(i**2)
#Cách 1
def isSnum(x):
    global res
    for i in range(len(res)):
        if res[i]>x: return False
        if x%res[i]==0: return True
    return False
for i in range(n):
    if isSnum(i):
        print(i,end=' ')

# # Cách 2
# check = [False for i in range(n)]

# for i in res:
#     for x in range(i,n,i):
#         # print(x,end=' ')
#         if check[x] == False:       
#             check[x] = True
#             print(x,end=' ')
        
