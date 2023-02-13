import math
import random 
def eratothenes(n):
    prime=[True for i in range(0,n+1)]
    prime[0] = False
    prime[1] = False
    p=2
    for p in range(2,n):
        if (prime[p]==True):
            for i in range(p+p,n+1,p):
                prime[i]=False
    return prime
            
        
eratothenes(97)
def eratothenesPhanDoan(n):
    prime=[True for i in range(0,n+1)]
    delta = round(math.sqrt(n))
    prime[0:(delta+1)] = eratothenes(delta)
    for i in range(delta*2,n,delta):
        for p in range(2,round(math.sqrt(i))):
            if prime[j]==True:
                pass
def isPrime(n):
    pass
#-----------------------------------------------------#  
def phanTichThuaSoNguyenTo(n):
    if isPrime(n):
        print(n,'= 1 *',n)
        return
    prime = []
    f = []
    p=2
    x = n
    while p<=x: 
        count=0
        while x%p ==0:
            x=int(x/p)
            count+=1
        if (count > 0):
            prime.append(p)
            f.append(count)
        p+=1
    print(prime)
    print(f)
#-----------------------------------------------------#  
def nhanBinhPhuongLap(a,k,n):
    b=1
    if (k==0):
        return (b)
    A = a
    t = round(math.log2(k))
    if (k%2==1):
        b=a
    k=k>>1
    for i in range(1,t+1):
        A = A**2 % n
        if (k%2==1):
            b = A*b % n
        k=k>>1
    return b
#-----------------------------------------------------#       
def getRandom(min,max):
    return round(random.random()*(max-min))+min 
def isPrimeMillerRabin(n):
    if (n==2): 
        return True
    if (n%2==0):
        return False
    #Phân tích n thành dạng r*2^s
    r = n-1
    s=0
    while (r%2==0):
       s+=1
       r = int(r/2)
    
    for i in range(10):
        a = getRandom(2,n-1)
        y = nhanBinhPhuongLap(a,r,n)
        if (y!=1) and (y!=(n-1)):
            j=1
            while (j<=s-1) and (y!=(n-1)):
                y = y**2 % n
                if y == 1:
                    return False
                j = j+1
            if y != (n-1):
                return False
    return True 
 


    
    
        
        
         
         
                
    
