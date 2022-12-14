import sys

sys.setrecursionlimit(30000)

input = sys.stdin.readline

n, m = map(int, input().split())

# 그니까 간단하게 정리하먄
# n*7이 넘지 않는다면 이때는 저중 가장 적은거 사용!
#
if n==1:
  print(1)
elif n==2:
  print(min(4, (m-1)//2 +1))
elif m <=6:
  print(min(4,m))
else:
  print(m-2)
