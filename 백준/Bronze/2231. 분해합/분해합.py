n = int(input())

result = 0
for i in range(1, n):
    tmp = i + sum(map(int, str(i)))
    if tmp == n:
        result = i
        break
        
print(result)