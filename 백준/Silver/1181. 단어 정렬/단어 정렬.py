n =int(input())
    
arr = []
min = 51
for i in range(n):
    arr.append(input())

arr = set(arr)
arr = list(arr)
arr.sort()
arr.sort(key=len, reverse=False)

for i in arr:
    print(f"{i}")
