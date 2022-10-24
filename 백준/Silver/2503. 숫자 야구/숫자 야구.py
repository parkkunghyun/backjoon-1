arr = []
result = []

for i in range(123, 1000):
    temp = str(i)
    if '0' in temp:
        pass
    elif len(list(set(temp))) == 3:
        arr.append(list(temp))
        result.append(list(temp))
        
for _ in range(int(input())):
    check_number, check_strike, check_ball = map(int, input().split())
    check_number = str(check_number)
    if len(arr) == 1:
        continue
        
    for number in arr:
        strike = 0; ball = 0
        List = list(check_number)
        for i in range(3):
            if number[i] == check_number[i]:
                List.remove(number[i])
                strike += 1
        ball += len(set(List) & set(number))
        
        if check_strike == strike and check_ball == ball:
            continue
        else:
            if number in result:
                result.remove(number)
            else: pass
            
print(len(result))