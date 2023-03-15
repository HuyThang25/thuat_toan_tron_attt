from Thu_Vien.soNguyenTo import *
from math import *

a = int(input('Nhập vào A: '))
b = int(input('Nhập vào B: '))

prime = eratothenes(b)

# Một số nguyên tố là một số lẻ (không xet số 2 vì không thoả mãn là tổng bình phương hai số nguyên tố)
# Mà một số lẻ = một số lẻ + một số chẵn
# Ta lại có một số lẻ bình phương lên cũng là số lẻ
# Do đó để thoả mãn số như trong đề bài thì 
#   Số đó phải là một số nguyên tố có tổng = 2^2 + k^2 (với k là số nguyên tố)
#       a<= 2^2+k^2 <=b 
#  <=> sqrt(a-4) <= k <= sqrt(b-4)
print("Các số thoả mãn: ")
for k in range(ceil(sqrt(max(0,a-4))),int(sqrt(b-4))+1):
    if prime[k]:
        if prime[k*k+4]:
            print(k*k+4,end=' ')

        


