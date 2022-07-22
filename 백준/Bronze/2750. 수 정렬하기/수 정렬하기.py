t = int(input())

list = []

for _ in range(t):
    list.append(int(input()))
x = sorted(list)

for i in range(len(x)):
    print(x[i])