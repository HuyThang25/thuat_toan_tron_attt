from phepToanVoiSoNguyenLon import *
p,w = 2147483647,8

a = int(input())
print(convertDecimalToWordByte(a,w,p))

b=[]
print("Nhập vào mảng: ")
for i in range(4):
   b.append(int(input())) 
print(convertWordByteToDecimal(b,w,p))