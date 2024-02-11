import sys
kb = sys.stdin
def kadane(vec):
    sum=0
    mx=-10000000
    for e in vec:
        sum=sum+e
        mx=max(sum,mx)
        if(sum<0):sum=0
        
    return mx
def max_con_cir(A):
    linear=kadane(A)

    total=sum(A)
    max_sum_wrap=total+kadane([-e for e in A])

    return linear if max_sum_wrap==0 else max(max_sum_wrap,linear)

n=int(kb.readline())
A=[int(e) for e in kb.readline().split()]
print(max_con_cir(A))