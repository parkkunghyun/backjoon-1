import sys
input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(map(int,input().strip())) for _ in range(N)]
max_width = min(N,M)
answer = 0
for i in range(N):
    for j in range(M):
        for k in range(max_width):
            if (i+k) < N and (j+k) < M and (board[i][j] == board[i+k][j] == board[i][j+k] == board[i+k][j+k]):
                answer = max(answer, (k+1)**2)
print(answer)
#for _ in range(n):
#    s = input()
#    j =[]
#    for i in range(len(s)):
#        j.append(int(s[i]))        
#    arrs.append(j)