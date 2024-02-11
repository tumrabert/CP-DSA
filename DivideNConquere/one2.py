import math

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
dt={0:0,
   1:1,
   2:2,
   3:3,
   4:4,
   5:5,
   6:6,
   7:6,
   8:5,
   9:4,
   10:3,
   11:2,}
def ones(n):
    if n<=11:
        return dt[n]
    
    #q=0
    j=0
    for i in range(1,len(k)):
        if k[i]<n:
            j=i
    floor = n/k[j]
    if(floor<=5.55):
        return ones(n-k[j])+ j
    else:
        return ones(k[j+1]-n)+(j+1)

n=int(input())
k=[0,1,11,111,1111,11111,111111,1111111,11111111,111111111,1111111111,11111111111]
print(ones(n))