import math

s= int(input())
m = 2
while s != 1:
    if s % m == 0:
        s = s/m
        print(m)
    else:
        m += 1