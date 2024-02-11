import sys
kb=sys.stdin
def kadane(A):
    mx=0
    sum=0
    for e in A:
        sum+=e
        mx=max(mx,sum)
        if(sum<0):sum=0
    return mx
        
n=int(input())
A=[int(e) for e in kb.readline().split()]

total_sum=sum(A)
max_ss=max(kadane(A),total_sum)
min_ss=min(kadane([-x for x in A]),0)
if(min_ss)!=0:
    max_ss=max(max_ss,total_sum+min_ss)

print(max_ss)