import sys
input = sys.stdin.readline
from collections import deque

di = [0, 0, 0, 1, -1]
dj = [0, 1, -1, 0, 0]
def bfs(start):
    cnt = 0
    q = deque()
    q.append(start)
    while q:
        a, b = q.popleft()
        for k in range(5):
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= ni < n and 0 <= nj < m and vis[ni][nj] == False and mat[ni][nj] == 1:
                cnt += 1
                vis[ni][nj] = True
                q.append((ni,nj))
    return cnt


n, m = map(int, input().split())
# n은 세로 m은 가로
mat = [list(map(int, input().split())) for _ in range(n)]
vis = [[False] * m for _ in range(n)]
one = []
total = 0
ch = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] == 1:
            one.append((i, j))
for i in one:
    a = bfs(i)
    if a > 0:
        if total < a:
            total = a
        ch += 1
print(ch)
print(total)



