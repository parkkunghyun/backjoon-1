import sys
import math 
t = int(sys.stdin.readline().strip())

def UC(x,y):
    while(y):
        x,y = y,x%y
    return x
def gcd(x,y):
    result = (x*y) // UC(x,y)
    return result

for i in range(t):
    n,m = map(int, sys.stdin.readline().split())
    if n >=m:
        print(gcd(n,m))
    else:
        print(gcd(m,n))