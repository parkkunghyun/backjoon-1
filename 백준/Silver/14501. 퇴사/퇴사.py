#import sys
#from collections import defaultdict
#sys.setrecursionlimit(300000)
import sys

sys.setrecursionlimit(30000)

input = sys.stdin.readline
n = int(input())
dp = [0 for _ in range(n + 1)]
t = [0 for _ in range(n + 1)]
p = [0 for _ in range(n + 1)]

for i in range(n):
    x, y = map(int, input().split())
    t[i] = x
    p[i] = y

for i in range(len(t) - 2, -1, -1):
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(p[i] + dp[t[i] + i], dp[i + 1])

print(dp[0])
