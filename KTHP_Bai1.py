def isQPrime(n):
    count =2
    for i in range(2,n):
        if n%i==0:
            count+=1
    return count==4
def laySoNguyenDuong():
    n = int(input())
    while n<=0:
        n = int(input('Vui lòng nhập vào một số nguyên dương: '))
    return n
print('Nhập vào số nguyên dương n: ',end='')
n = laySoNguyenDuong()
emty = True
print(f"Các số Q-Prime nhỏ hơn hoặc bằng {n} là: ")
for i in range(2,n+1):
    if isQPrime(i): 
        emty = False
        print(i,end=' ')
if emty:
    print("Không có số nào")