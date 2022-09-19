s = input()

arr =[]

for i in s:
    k = int(i)
    arr.append(i)

arr.sort(reverse=True)
j =""
for i in arr:
    k = str(i)
    j+=k 
print(j)
    

