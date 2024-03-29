def div_and_mod(a,b):  
    dec_a = int(a,2)
    dec_b = int(b,2)
    bin_a = bin(dec_a)[2:]
    bin_b = bin(dec_b)[2:]
    dec_thuong = 0
    while len(bin_a) >= len(bin_b) and (dec_a != 0):
        dec_thuong = dec_thuong+(1<<(len(bin_a)-len(bin_b))) #thương = thương + x^(bậc a(x) - bậc b(x))
        dec_a = dec_a^(dec_b<<(len(bin_a)-len(bin_b))) # a(x) = a(x) - x^(bậc a(x) - bậc b(x))*b(x)
        bin_a = bin(dec_a)[2:] # gán lại giá trị bin_a khi dec_a thay đổi
    return bin(dec_thuong)[2:],bin_a # trả về thương và dư 

def add(a,b):
    return bin(int(a,2)^int(b,2))[2:] #phép cộng giưa hai đa thức thực chất là phép xor giữa hai số nhị phân
def multi(a,b,gx):
    dec_a = int(a,2)
    dec_b = int(b,2)
    dec_res=0
    for i in range(len(b)):
        if b[i]=='1':
            dec_res = dec_res^(dec_a<<(len(b)-1-i)) #nhân hàm a(x) với từng phần tử của hàm b(x) r cộng lại
    tmp_div,tmp_mod = div_and_mod(bin(dec_res)[2:],gx)
    return tmp_mod
def display(a):
    if a == '1': print('1')
    elif a== '0': print('0')
    else:
        vt = 0
        for i in range(len(a)):
            if a[i] =='1':
                if i==len(a)-1:
                    print('1',end=' ')
                else:
                    print(f'x^{len(a)-1-i}',end=' ')   
                vt = i
                break
        for i in range(vt+1,len(a)):
            if a[i]=='1':
                if i == len(a)-1:
                    print('+ 1',end=' ')
                else:
                    print(f'+ x^{len(a)-1-i}',end=' ')
def extendEuclid(a,b):
    (u,v) = (a,b)
    (x1,x2) = ('0','1')
    (y1,y2) =('1','0')
    while v !='0':
        (q, r) = div_and_mod(u,v)
        (x, y) =  (add(x2, multi(q,x1,b)), add(y2, multi(q,y1,a))) # trong đa thức thì cộng trừ là một vd 0 - x = -x = (-1 mod 2)x = x
        (x1, x2, y1, y2) = (x, x1, y, y1)
        (u, v) = (v, r)
    return (u,x2,y2)
a = input('Nhập vào a(x): ')
g = input('Nhập vào g(x): ')
gcd,nghich_dao_a,nghich_dao_g = extendEuclid(a,g) 
if gcd=='1':
    print('Nghịch đảo a(x) = ',end='')
    display(nghich_dao_a)
else:
    print('Không có nghịch đảo')        
        