n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

cnt = 0
for i in range(n - 1, 0, -1):
    if arr[i] <= arr[i - 1]:
        #print(arr[i], arr[i - 1])
        k = arr[i] - 1
        cnt += arr[i - 1] - k
        arr[i - 1] = k

print(cnt)
