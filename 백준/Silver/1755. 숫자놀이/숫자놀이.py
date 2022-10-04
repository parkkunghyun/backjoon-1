m,n= map(int, input().split())
# zero one two three four five six seven eight night 

# eight five four night one seven six three two zero

def numChangeStr(i):
    word=""
    if i ==0:
        word = "zero"
    elif i ==1:
        word = "one"
    elif i ==2:
        word="two"
    elif i ==3:
    	word="three"
    elif i ==4:
        word="four"
    elif i ==5:
        word="five"
    elif i ==6:
        word="six"
    elif i ==7:
        word="seven"
    elif i ==8:
        word="eight"
    elif i ==9:
        word="nine"
    return word

def strChangeNum(i):
    num = 0
    if i == "zero":
        num = 0
    elif i == "one":
        num = 1
    elif i == "two":
        num = 2
    elif i == "three":
        num = 3
    elif i == "four":
        num = 4
    elif i == "five":
        num = 5
    elif i == "six":
        num = 6
    elif i == "seven":
        num = 7
    elif i == "eight":
        num = 8
    elif i == "nine":
        num = 9
    return num

arr = [[""]*2 for i in range(100)]

for i in range(m,n+1):
    if i >=10:
        x =0
        y = 0
        if i % 10 ==0:
        	x = i //10
        else:
        	x = i//10
        	y = i % 10
        
        arr[i][0] = numChangeStr(x)
        arr[i][1] = numChangeStr(y)
    else:
        arr[i][0] = numChangeStr(i)
        arr[i][1] = ""
        
arr.sort()
brr =[]
for i in range(len(arr)):
    if arr[i][0] !="":
        if arr[i][1] !="":
            x = strChangeNum(arr[i][0])
            y = strChangeNum(arr[i][1])
            sum = x*10 + y
            brr.append(sum)
        else:
            x = strChangeNum(arr[i][0])
            brr.append(x)
            
cnt = 0
for i in range(len(brr)):
    print(brr[i], end=" ")
    cnt+=1
    if cnt ==10:
        print()
        cnt = 0