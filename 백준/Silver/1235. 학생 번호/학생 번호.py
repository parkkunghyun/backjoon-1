n = int(input())
cnt = 0
arr = []
for i in range(n):
    s = input()
    arr.append(s)
for i in range(1,len(arr[0])+1):
    results = []
    for j in range(n):
        if arr[j][-i:] in results:
            break
        else:
            results.append(arr[j][-i:])
    if len(results)==n:
        print(i)
        break