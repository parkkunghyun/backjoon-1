n = int(input())

x =[]
y =[]
index=[]

for z in range(n):
    i= list(map(int,input().split()))
    index.append(i)

indexSort=[] 
index.sort()
for i in range(n):
    k= index[i][0]
    j = index[i][1]
    print(k,j)