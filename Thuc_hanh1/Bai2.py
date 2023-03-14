from phepToanVoiSoNguyenLon import *
(w,p)=(8,2147483647)
a = int(input())
b = int(input())
arrA = convertDecimalToWordByte(a,w,p)
arrB = convertDecimalToWordByte(b,w,p)
e,sum = addition(arrA,arrB,w,p)
print(sum)