import sys
kb=sys.stdin
def P(l,M):
    return S[M]-(0 if l==0 else S[l-1])+(M-l+1)*k

def cut(l,b): 
    L,R=0,n-1
    res=-1
    while(L<=R):
        M=(L+R)//2
        '''if(P(l,M)==b):
            res=M
            break'''
        if(P(l,M)<=b):
            res=M
            L=M+1
        else:
            R=M-1
    r=res

    return 0 if r==-1 else S[r]-(0 if l==0 else S[l-1])

n,m,k = list(map(int,kb.readline().split()))
A= list(map(int,kb.readline().split()))
S=list()
sum=0
for e in A:
    sum+=e
    S.append(sum)

for i in range(m):
    l,b= list(map(int,kb.readline().split()))
    print(cut(l,b))