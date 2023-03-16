from Thu_Vien.soNguyenTo import *
from math import *
def main():
    n = int(input('Nhập vào n: '))
    prime = eratothenes(n)
    res = []
    for i in range(n):
        if prime[i]:
            res.append(i)
    for i in range(0,len(res)-2):
        for j in range(i+1,len(res)-1):
            if res[i]+res[j] >= n: break
            for k in range(j+1,len(res)):
                tmp = res[i] + res[j] + res[k]
                if tmp == n:
                    print(f'{n} = {res[i]} + {res[j]} + {res[k]}')
                if tmp > n:
                    break
main()