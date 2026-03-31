import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
CF AC link: https://codeforces.com/contest/1712/submission/369045717

Goal is to maximize the distance of the shortest path between any two nodes
Only have to consider paths from node i to i+1 (by condition all other pairs cannot be longer)
if n = 2, minimum value is forced
if n >= 4, always possible to choose adjacency not containing the minimal;
then condition for diameter of at least x is change anything under x/2,
then walk through each adjacency and check the min changes needed to have 
any adjacency with both values at least x

if n = 3:
- k = 3 implies 1000000000
- k = 0 is brute force
- actually just brute force this
"""

def f(n,k,ar,x):
    h = [0]*n # operations used and where
    left = k
    # a -> c -> b cases
    for i in range(n):
        if ar[i] < (x+1)//2:
            left -= 1
            h[i] = 1
            if left == -1: return False
    # a -> b direct cases
    extra = 2
    for i in range(n-1):
        a = ar[i]
        b = ar[i+1]
        if h[i] == 1: a = 1000000000
        if h[i+1] == 1: b = 1000000000        
        if a >= x and b >= x: 
            extra = 0
            break
        elif a >= x or b >= x: extra = 1
    left -= extra
    return left >= 0

def g(ar): # edge case for n = 3
    return max(min(ar[0],ar[1],ar[2]*2),min(ar[0]*2,ar[1],ar[2]))

for _ in range(readint()):
    n,k = readints()
    ar = readar()
    if n == 2:
        if k == 0: print(min(ar))
        elif k == 1: print(max(ar))
        else: print(1000000000)
    elif n == 3:
        # do things here
        a,b,c = ar[0],ar[1],ar[2]
        if k >= 3: print(1000000000)
        else:
            br = [[a,b,c]]
            if k == 1: br = [[1000000000,b,c],[a,1000000000,c],[a,b,1000000000]]
            elif k == 2: br = [[1000000000,1000000000,c],[a,1000000000,1000000000],[1000000000,b,1000000000]]
            ans = 0
            for b in br:
                ans = max(ans,g(b))
            print(ans)
    else:
        low = 1 # answer must always be at least this
        high = 1000000000 # answer can never exceed this
        while high-low > 1:
            mid = (low+high)//2
            if f(n,k,ar,mid): low = mid
            else: high = mid
        if f(n,k,ar,high): print(high)
        else: print(low)
