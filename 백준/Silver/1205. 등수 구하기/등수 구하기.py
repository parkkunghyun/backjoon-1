n,tScore,p = map(int,input().split())

if n ==0:
    print(1)
else:
    score = list(map(int,input().split()))
    if n == p and score[-1] >=tScore:
        print(-1)
    else:
        res = n+1
        for i in range(n):
            if score[i] <= tScore:
                res = i+1
                break
        print(res)