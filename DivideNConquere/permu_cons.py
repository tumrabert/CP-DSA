
def permu(n,ans=[]):
    if(len(ans)==n):
        print(" ".join(map(str,ans)))
        return
    for i in range(n):
        if i not in ans:
            if i in B:
                a=dt[i]
                if(a not in ans):
                    continue
                else:
                    ans.append(i)
                    permu(n,ans)
                    ans.pop()
            else:
                ans.append(i)
                permu(n,ans)
                ans.pop()
            
n, m = list(map(int,input().split()))
dt=dict()
B=list()
A=list()
for i in range(m):
    a,b=list(map(int,input().split()))
    B.append(b)
    A.append(A)
    dt[b]=a
a=list()
permu(n,a)