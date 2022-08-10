l = ['c=','c-', 'dz=','d-','lj','nj' ,'s=','z=']

count =0
s = input()
for i in l:
    s = s.replace(i,'*')
print(len(s))