from Thu_Vien.phepToanVoiSoNguyenLon import *
(w,p)=(8,2147483647)
a = int(input())
b = int(input())
arrA = convertDecimalToWordByte(a,w,p)
arrB = convertDecimalToWordByte(b,w,p)
e,sub=subtraction(arrA,arrB,w,p)
print(sub)
