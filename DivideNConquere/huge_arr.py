import sys
kb=sys.stdin
n,q= [int(e) for e in kb.readline().split()]
S=list()
sum_arr=list()
def bin_search_idx(arr,num):
    l=0
    r=len(arr)-1
    while(l<r):
        m=(l+r)>>1
        if(num==arr[m]):
            return m
        
        if(arr[m]<num):
            l=m+1
        else:
            r=m
    if(l==r):return r
for i in range(n):
    S.append([int(e) for e in kb.readline().split()])
K=sorted(S)
s=0
for a,b in K:
    s=s+b
    sum_arr.append(s)
#print(sum_arr)
#print(K)
for i in range(q):
    num=int(kb.readline())
    idx=bin_search_idx(sum_arr,num)
    print(K[idx][0]) 