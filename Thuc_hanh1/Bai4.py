from phepToanVoiSoNguyenLon import *
w=8
p = int(input('Nhập vào p: '))
a = int(input('Nhập vào a: '))
b = int(input('Nhập vào b: '))
print('Ma trận P =',convertDecimalToWordByte(p,w,p))

arrA = convertDecimalToWordByte(a,w,p)
arrB = convertDecimalToWordByte(b,w,p)
print('Cộng chính xác bôi a và b:',addition(arrA,arrB,w,p))

e,sum = additionInFp(arrA,arrB,w,p)
print('Cộng trên trường Fp:',sum)
