import sys

sys.setrecursionlimit(30000)
input = sys.stdin.readline

n = int(input())
ans = list(map(int, input().split()))
ans.sort()

if len(ans) % 2 == 0:
  mid = len(ans) // 2
  midMinus = len(ans) // 2 - 1
  count1 = 0
  count2 = 0
  for i in range(len(ans)):
    count1 += abs(ans[i] - ans[mid])
    count2 += abs(ans[i] - ans[midMinus])
  if count1 < count2:
    print(ans[mid])
  else:
    print(ans[midMinus])
else:
  mid = len(ans) // 2
  count1 = 0
  for i in range(len(ans)):
    count1 += abs(ans[i] - ans[mid])
  print(ans[mid])
