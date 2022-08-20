n,k = map(int,input().split())
x = list(map(int,input().split()))

x.sort()
print(x[len(x)-k])
# 76 85 93 98 100

