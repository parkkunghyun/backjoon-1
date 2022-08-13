n,m =map(int,input().split())

l = list(map(int, input().split()))

interval_sum = 0
end = 0
count =0
    
for start in range(n):
    
    while end <n and interval_sum <m:
        interval_sum += l[end]
        end += 1
        
    if interval_sum == m:
        count += 1
    interval_sum -= l[start]
print(count)