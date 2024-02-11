import sys
kb=sys.stdin
n,m= [int(e) for e in kb.readline().split()]
L= [int(e) for e in kb.readline().split()]
def find(nn,r,c):
    #basecase
    if(nn==2):
        return L[2*r+c-3]
    
    mid=nn//2
    
    if r<=mid:
        if c<=mid:
            return find(mid,r,c)
        else:
            return find(mid,c-mid,r)
            #print("Q2")
    else:
        if c<=mid:
            return find(mid,r-mid,c)*-1
            #print("Q3")
        else:
            return find(mid,c-mid,r-mid)*-1
            #print("Q4")

for i in range(m):
    r,c= [int(e) for e in kb.readline().split()]
    ans=find(1<<n,r,c)
    print(ans)