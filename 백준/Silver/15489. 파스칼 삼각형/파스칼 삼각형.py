r, c, w = map(int, input().split())

arr = [[0], [1], [1, 1]]
cnt = 0
for i in range(2, r + w):
  newArr = []
  newArr.append(1)
  for j in range(1, len(arr[i])):
    newArr.append(arr[i][j - 1] + arr[i][j])
  newArr.append(1)
  arr.append(newArr)

sum = 0
cnt = c
for i in range(r, r + w):
  for j in range(c - 1, cnt):
    #print(arr[i][j])
    sum += arr[i][j]
  cnt += 1



print(sum)

