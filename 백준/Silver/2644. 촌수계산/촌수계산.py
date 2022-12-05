#import sys
#from collections import defaultdict
#sys.setrecursionlimit(300000)
import sys

sys.setrecursionlimit(30000)

input = sys.stdin.readline


def dfs(L):
    for i in pArray[L]:
        if check[i] == 0:
            check[i] += check[L] + 1
            dfs(i)


n = int(input())
a, b = map(int, input().split())

pArray = [[] for _ in range(n + 1)]
check = [0 for _ in range(n + 1)]

for _ in range(int(input())):
    c, d = map(int, input().split())
    pArray[c].append(d)
    pArray[d].append(c)

dfs(a)
if check[b] == 0:
    print(-1)
else:
    print(check[b])


