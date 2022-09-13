import sys

#input = sys.stdin.readline()
n,m = map(int,input().split())

packages = [0 for _ in range(m)]
words=[0 for _ in range(m)]

for i in range(m):
    p,w = map(int,input().split())
    packages[i] = p 
    words[i]=w
    
minPackage = min(packages)
minWord = min(words)

sums =[]
a = n//6
b = n%6

sum1 = a*minPackage + b*minWord
sums.append(sum1)
sum2 = (a+1)*minPackage
sums.append(sum2)
sum3 = n*minWord
sums.append(sum3)

print(min(sums))

 