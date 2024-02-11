import sys
kb=sys.stdin

def mcs(l,r):
    if l==r:
        return A[l]
    mid =(l+r)//2
    r1=mcs(l,mid)
    r2=mcs(mid+1,r)
    msl = -1*float('inf')
    sl=0
    for i in range(mid,l-1,-1):
        sl+=A[i]
        msl=max(msl,sl)
    msr = -1*float('inf')
    sr=0
    for j in range(mid+1,r+1):
        sr+=A[j]
        msr=max(msr,sr)
    r3=msl+msr
    #print(r1,r2,r3)
    return max(r1,r2,r3)
def mcs2(L,R):
    if L==R:
        return mcs(L,R)
    M =(L+R)//2
    R1=mcs(L,M)
    R2=mcs(M+1,R)

    MSL=-1*float('inf')
    SL=0
    for i in range(M,L-1,-1):
        SL+=A[i]
        MSL=max(MSL,SL)

    MSR=-1*float('inf')
    SR=0
    for j in range(M+1,R+1):
        SR+=A[j]
        MSR=max(MSR,SR)
    R3=MSL+MSR
    R12=R1+R2
    R13=R1+R3
    #R23=R2+R3
    print(R1,R2,R3,R12,R13)
    return max(R1,R2,R3,R12,R13)

max_r1,max_r2,max_r3= -float('inf'), -float('inf'), -float('inf')       
n=int(input())
A=[int(e) for e in kb.readline().split()]
S=[]
sum=0
for e in A:
    sum+=e
    S.append(sum)
ans=mcs2(0,n-1)
print(ans)
#print(max_r1,max_r2,max_r3)

'''mx=-1*float('inf')
for i in range(n):
    L=A[:i]
    R=A[i:]
    sumL=mcs(L)
    sumR=mcs(R)
    mx=max(mx,sumL+sumR)
print(mx)'''
#print(mcs(A))