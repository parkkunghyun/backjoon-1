while True:
    a,b,c = map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    else:
        if a > b and a>c:
            if (c*c)+(b*b) == a*a:
                print('right')
            else:
                print('wrong')
        elif b>a and b >c:
            if (c*c)+(a*a) == b*b:
                print('right')
            else:
                print('wrong')
        elif c>a and c>a:
            if (a*a)+(b*b) == c*c:
                print('right')
            else:
            	print('wrong')