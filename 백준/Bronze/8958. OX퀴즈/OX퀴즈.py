t = int(input())

for _ in range(t):
    sum =0
    ox = str(input())
    plus = 0
    for i in ox:
        if i == "O":
            plus += 1
            sum += plus
        elif i == "X":
            plus = 0
    print(sum)