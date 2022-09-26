s = input()
a = 'AAAA'
b = 'BB'
arr =[]
result = ''
j = ''

for i in s:
    if i =='.':
        arr.append(j)
        j=''
        arr.append(i)
    else:
        j+='X'

arr.append(j)

    
for i in arr:
    if len(i) %2 != 0 and i != '.':
        result =''
        break
    if i =='.':
        result += '.'
    else:
        if len(i)==2:
            result += 'BB'
        else:
            k = len(i) //4
            z = len(i) %4
            z = z//2
            result +=k*a + z*b
if result =='':
    print(-1)
else:
    print(result)
        
        

    