import math

def M(N):
    return 2**(int(math.log(N,2)) + 1) - 1

def C(N, L, R):
    if N == 0: return 0
    if N == 1: return 1
    if L > R: return 0
    m = M(N//2)
    c = 0
    if R < m+1:
        return C(N//2, L, R)
    elif R == m+1:
        return N%2 + C(N//2, L, m)
    elif L > m+1:
        return C(N//2, L-m-1, R-m-1)
    elif L == m+1:
        return N%2 + C(N//2, 1, R-m-1)
    else:
        return C(N//2, L, m) + N%2 + C(N//2, 1, R-m-1)

N, L, R = [int(e) for e in input().split()]
print(C(N, L, R))