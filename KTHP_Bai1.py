def isQPrime(n):
    count =2
    for i in range(2,n):
        if n%i==0:
            count+=1
    return count==4
n = int(input())
for i in range(2,n+1):
    if isQPrime(i): 
        print(i,end=' ')