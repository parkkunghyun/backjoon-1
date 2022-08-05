N = int(input())  # 나누어지는 수
d = 2  # 나누는 수

while N != 1:
    if N % d != 0:
        d += 1
    else:
        N //= d
        print(d)