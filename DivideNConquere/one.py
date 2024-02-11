import math
n=int(input())
k=[1,11,111,1111,11111,111111,1111111,11111111,111111111,1111111111,11111111111]
def q(n):
    l, r=0,len(k)-1
    result=-1
    while(l<=r):
        mid=(l+r)//2
        if(k[mid]<=n):
            result=k[mid]
            l=mid+1
        else:
            r=mid-1
    return result
def qk(n):
    l, r=0,len(k)-1
    result=float('inf')
    while(l<=r):
        mid=(l+r)//2
        if(k[mid]>n):
            result=min(result,k[mid])
            r=mid-1
        else:
            l=mid+1
    return result
def F(n):
    if(n==0):
        return 0
    if(n in k):
        return k.index(n)+1

    QN=q(n)
    Ta=math.floor(n/QN)
    a=Ta*QN
    A=Ta*F(QN)+F(n-a)

    QK=qk(n)
    Tb=1
    B=Tb*F(QK)+F(Tb*QK-n)
    return min(A,B)
print(q(n),qk(n))
print(F(n))