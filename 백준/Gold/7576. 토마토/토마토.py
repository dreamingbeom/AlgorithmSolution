import sys
input = sys.stdin.readline
from collections import deque
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def bfs(start):
    cnt = -1
    q = deque()
    for i in one:
        q.append(i)
    while q:
        z = len(q)
        cnt += 1
        for i in range(z):
            a, b = q.popleft()
            for k in range(4):
                ni = a + di[k]
                nj = b + dj[k]
                if 0 <= ni < n and 0 <= nj < m and vis[ni][nj] == False and mat[ni][nj] == 0:
                    vis[ni][nj] = True
                    q.append([ni, nj])
    return cnt

m, n = map(int, input().split())
# m은 가로 n은 세로
mat = [list(map(int, input().split())) for _ in range(n)]
vis = [[False] * m for _ in range(n)]
ch = 0
one = []
for i in range(n):
    for j in range(m):
        if mat[i][j] == 1:
            one.append((i,j))
            vis[i][j] = True
        elif mat[i][j] == 0:
            ch += 1
        else:
            vis[i][j] = True
if ch == 0:
    ch = False

total = bfs(one)
ch2 = 0
for i in range(n):
    for j in range(m):
        if vis[i][j] == False:
            ch2 += 1
if ch2 > 0:
    ch2 = True


if ch == False:
    print(0)
elif ch2 == True:
    print(-1)
else:
    print(total)




