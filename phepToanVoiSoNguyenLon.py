import math
(w,p)=(8,2**31)
def convertDecimalToWordByte(n,w,p):
    m= round(math.log(p,2))
    t = round(m/w)
    a=[]
    for i in range(0,t):
        a.append((n>>(w*i))&0xff)
    a.reverse()
    return a 
def convertWordByteToDecimal(a,w,p):
    n=0
    m= round(math.log(p,2))
    t = round(m/w)
    for i in range(0,t):
        n=(n<<w) +a[i]
    return n
def addition(arrA,arrB,w,p):
    arrA.reverse()
    arrB.reverse()
    c=[]
    m= round(math.log(p,2))
    t = round(m/w)
    e=0
    for i in range(0,t):
        c.append((arrA[i]+arrB[i]+e)&0xff)
        e=((arrA[i]+arrB[i]+e)>>8)&1
    c.reverse()
    return (e,convertWordByteToDecimal(c,w,p))
def subtraction(arrA,arrB,w,p):
    arrA.reverse()
    arrB.reverse()
    c=[]
    m= round(math.log(p,2))
    t = round(m/w)
    e=0
    for i in range(0,t):
       c.append((arrA[i]-arrB[i]-e)&(2**w-1))
       e=((arrA[i]-arrB[i]-e)>>8)&1
    c.reverse()
    return (e,c)
def multiprecision(arrA,arrB,w,p):
    arrA.reverse()
    arrB.reverse()
    m= round(math.log(p,2))
    t = round(m/w)
    c=[0 for i in range(0,2*t)]
    for i in range(0,t):
        u=0
        for j in range(0,t):
            sum = c[i+j] +arrA[i]*arrB[j]+u
            u = sum>>w
            c[i+j] = sum&0xff
        c[i+t] = u
    c.reverse()
    print(c)
    return (c)
def squaring(a,w,p):
    return multiprecision(a,a,w,p)

a = [157, 0, 173, 23]
b = [169, 1, 0, 64]
res = [1,70, 1, 173, 87]
c = [70, 1, 173, 87]
print(a,' = ',convertWordByteToDecimal(a,w,p))
print(b,' = ',convertWordByteToDecimal(b,w,p))
print('a + b = ',convertWordByteToDecimal(a,w,p)+convertWordByteToDecimal(b,w,p))
print( res,' = ',convertWordByteToDecimal(res,w,2**40)%p)
print('c = ',convertWordByteToDecimal(c,w,p))


    