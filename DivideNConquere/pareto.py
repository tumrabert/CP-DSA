n=int(input())
point=[]
for i in range(n):
    x,y=[int(e) for e in input().split()]
    point.append((x,y))

#point.sort(reverse=True)
count=1
maxy=point[0][1]
for x,y in point[1:]:
    if(y>maxy):
        maxy=y
        count+=1
print(count)
