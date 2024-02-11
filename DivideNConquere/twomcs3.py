import sys
kb=sys.stdin

def mcs2(L,R):
    if L==R:
        return A[L]
    M =(L+R)//2
    R1=mcs2(L,M)
    R2=mcs2(M+1,R)

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
    print(R1,R2,R3,R1+R2,MSL,MSR)
    return max(R1,R2,R3)

max_r1,max_r2,max_r3= -float('inf'), -float('inf'), -float('inf')       
n=int(input())
A=[int(e) for e in kb.readline().split()]
S=[]
sum=0
for e in A:
    sum+=e
    S.append(sum)
print(mcs2(0,n-1))
