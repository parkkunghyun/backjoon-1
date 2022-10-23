import sys

input = sys.stdin.readline

n = int(input())
books = {}
for _ in range(n):
    book = input().split('\n')[0]
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1


b1 = sorted(books.items(),key=lambda x: (x[1],x[0]))

answer = b1[-1][0]
nu = b1[-1][1]

c = []
c.append(answer)
f = False
for i in range(len(b1)-1):
  if b1[i][1] == nu:
    c.append(b1[i][0])


c.sort()
answer = c[0]
print(answer)