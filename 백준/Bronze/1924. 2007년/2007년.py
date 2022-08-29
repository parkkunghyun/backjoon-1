day=0
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
dates =[31,28,31,30,31,30,31,31,30,31,30,31]

n,m = map(int,input().split())

for i in range(0,n-1):
    day += dates[i]
    
sum = (day+ m)%7

print(week[sum])