import sys
kb=sys.stdin
""" def bin_search(L,R):
    pass """
n,m,k,w = [int(e) for e in kb.readline().split()]
p=[int(e) for e in kb.readline().split()] # monster in which channel 
h=[int(e) for e in kb.readline().split()] # h[i] for each life of monster
t=[int(e) for e in kb.readline().split()] # tower in which channel
""" S=[]
sum_of_power=[]
sum=0 
for i in range(m):
    
    S.append([p[i],h[i]])
S.sort()
for e in S:
    sum=sum+e[1]
    sum_of_power.append(sum)

print(S,sum_of_power)
print(t) """
for i in range(k):
    for j in range(m):
        if t[i]-w<=p[j]<=t[i]+w:
            h[j]-=1
            break
print(sum(h))

    #L=0 if t[i]-w <0 else t[i]-w
    #R=n-1 if t[i]+w > n else t[i]+w
    #bin_search(L,R) 