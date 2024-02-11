import sys
def bin_search(num,vec):
    l=0
    r=len(vec)-1
    result=-1
    if(num==vec[-1]):return r
    if (num==vec[0]):return l
    while(l<=r):
        
        m=(l+r)//2
       
        if num==vec[m]:
            return m
        elif(num<vec[m]):
            #result=r
            r=m-1
            
        else:
            result=l
            l=m+1
            
        
    return result
        
def bin_search_rec(l,r,num,vec):
    if(num<vec[0]):return -1
    if(num>=vec[-1]):return len(vec)-1
    mid=(l+r)>>1
    if(l==r):
        if(vec[l]<=num):return l #number more than Left
        else: return l-1

    if(vec[mid]<=num):
        return bin_search_rec(mid+1,r,num,vec)
    else:
        return bin_search_rec(l,mid,num,vec)

kb = sys.stdin
n,m=map(int,kb.readline().split())
N = [int(e) for e in kb.readline().split()]
M = [int(e) for e in kb.readline().split()]

for e in M:
    ans=bin_search_rec(0,n-1,e,N)
    print(ans)