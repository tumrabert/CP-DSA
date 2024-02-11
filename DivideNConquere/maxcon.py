import sys
kb = sys.stdin
def mcs(vec):
    sum=0
    mx=-10000000
    for e in vec:
        sum=sum+e
        mx=max(sum,mx)
        if(sum<0):sum=0
        
    return mx
n=int(kb.readline())
A=[int(e) for e in kb.readline().split()]
print(mcs(A))