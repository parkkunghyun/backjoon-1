#15988

import sys

sys.setrecursionlimit(30000)
input = sys.stdin.readline

dp = [0] * (1000001)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, len(dp)):
  dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
  if dp[i] >= 1000000009:
    dp[i] = dp[i] % 1000000009

t = int(input())
for _ in range(t):
  n = int(input())
  print(dp[n])
