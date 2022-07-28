n,k = map(int,input().split())

l = []
count = 0
backtick = n-1
for i in range(n):
    number = int(input())
    l.append(number)
    
for i in reversed(range(n)):
    count += k // l[i]
    k = k%l[i]
            
print(count)