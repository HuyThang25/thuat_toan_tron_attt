def backTrack(p,T):
    for i in range(0,len(T)-len(p)+1):
        if p[0] == T[i]:
            if p==T[i:i+len(p)]:
                return i
    return -1
#--------------------------------------------------#
def lastOccurrence(p,T):
    x = list(set(T))
    x.sort()
    f = []
    for i in range(len(x)):
        vt=-1
        for j in range(len(p)-1,-1,-1):
            if p[j]==x[i]: 
                vt = j
                break
        f.append(vt)
    return x,f
    
def Boyer_Moore(p,T):
    x,f = lastOccurrence(p,T)
    L = dict(zip(x,f))
    i = len(p)-1
    j = len(p)-1
    while(i<len(T)):
        while (j>=0) and (T[i]==p[j]): 
            i-=1
            j-=1
        if (j==-1): 
            return i+1
        else: 
            i = i+len(p)-min(j,1+L[T[i]])
            j = len(p)-1
    
    
def failure(p):
    f = [-1]
    for i in range(1,len(p)):
        count = 0
        for j in range(1,i):
            if p[0:j] == p[i-j:i]:
                count = j
        f.append(count)
    return f

                

def Knuth_Morris_Pratt(p,T):
    f = failure(p)
    i=0
    j=0
    while(i<=(len(T)-len(p))):
        while (j<len(p)) and (p[j]==T[i+j]):
            j+=1
        if j == len(p):
            return i
        else:
            i = i+j-f[j]
            if f[j]==-1: j=0
            else: j = f[j]
    return -1
print(Boyer_Moore('aabcab','abacaabadcabacabaabb'))