a,b,v = map(int, input().split())

sum = (v-b) / (a-b)
if sum == int(sum):
    print(int(sum))
else:
    print(int(sum)+1)