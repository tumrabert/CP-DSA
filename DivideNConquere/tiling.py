import sys
kb = sys.stdin


def tiling(a,b,L,missing):
    #basecase
    X,Y = missing
    #print("X-Y",X,Y)
    # Base case: If the current tile is 2x2
    #if (x2 - x1 == 1) and (y2 - y1 == 1):
    if (L == 2):
        dx=X-a
        dy=Y-b
        p=2*dy+dx
        print(p, a, b)
        return
    #check which Q of missing?
    mid=L//2
    
    posX=a+mid-1
    posY=b+mid-1
    if(X<a+mid and Y<b+mid):#Q1
        print(0,posX,posY)
        #tiling(a,b,L,missing)
        tiling(a,b,mid,missing) #Q1
        tiling(a+mid,b,mid,(a+mid,b+mid-1))#Q2
        tiling(a,b+mid,mid,(a+mid-1,b+mid))#Q3
        tiling(a+mid,b+mid,mid,(a+mid,b+mid))#Q4
    elif(X>=a+mid and Y<b+mid):#Q2
        print(1,posX,posY)
        tiling(a,b,mid,(a+mid-1,b+mid-1)) #Q1
        tiling(a+mid,b,mid,missing)#Q2
        tiling(a,b+mid,mid,(a+mid-1,b+mid))#Q3
        tiling(a+mid,b+mid,mid,(a+mid,b+mid))#Q4
    elif(X<a+mid and Y>=b+mid):#Q3
        print(2,posX,posY)
        tiling(a,b,mid,(a+mid-1,b+mid-1)) #Q1
        tiling(a+mid,b,mid,(a+mid,b+mid-1))#Q2
        tiling(a,b+mid,mid,(missing))#Q3
        tiling(a+mid,b+mid,mid,(a+mid,b+mid))#Q4
    else:#Q4
        print(3,posX,posY)
        tiling(a,b,mid,(a+mid-1,b+mid-1)) #Q1
        tiling(a+mid,b,mid,(a+mid,b+mid-1))#Q2
        tiling(a,b+mid,mid,(a+mid-1,b+mid))#Q3
        tiling(a+mid,b+mid,mid,(missing))#Q4
    
    #recur
L,x,y=[ int(e) for e in kb.readline().split()]
print(L*L//3)
tiling(0,0,L,(x,y))
""" tiling(m,n,L,(2,0))
tiling(m,n,L,(3,0))
tiling(m,n,L,(2,1))
tiling(m,n,L,(3,1)) """