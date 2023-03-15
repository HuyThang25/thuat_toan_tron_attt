from Thu_Vien.soNguyenTo import *
from math import *
def main():
    n = int(input('Nhập vào n: '))
    prime = eratothenes(n)
    res = []
    for i in range(n):
        if prime[i]:
            res.append(i)
    for i in range(0,len(res)):
        for j in range(0,len(res)):
            if res[i]+res[j] >= n: break
            for k in range(0,len(res)):
                tmp = res[i] + res[j] + res[k]
                if tmp == n:
                    print(f'{n} = {res[i]} + {res[j]} + {res[k]}')
                    return
                if tmp > n:
                    break
main()