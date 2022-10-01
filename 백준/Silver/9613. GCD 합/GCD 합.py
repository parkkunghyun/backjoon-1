import sys
t= int(input())
import math 

def gcd(n,m):
    smalll = 0
    result =0
    if n >= m:
        small = m
    else: 
        small = n
    for i in range(1,small+1):
        if(n%i ==0) and (m%i ==0):
            result = i
    return result
            

for i in range(t):
    arr = list(map(int,sys.stdin.readline().split()))
    arr = arr[1:]
    sum = 0    
    for x in range(len(arr)):
        for y in range(x+1,len(arr)):
            sum+= math.gcd(arr[x],arr[y])
    print(sum)
    