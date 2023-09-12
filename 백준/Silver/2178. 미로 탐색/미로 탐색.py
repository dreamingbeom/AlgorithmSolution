import sys
input = sys.stdin.readline
from collections import deque

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]
def bfs(start):
    q = deque()
    q.append(start)
    while q:
        a, b = q.popleft()
        if vis[a][b] == False:
            vis[a][b] = True
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= ni < n and 0 <= nj < m and vis[ni][nj] == False and mat[ni][nj] == 1:
                vis[ni][nj] = True
                mat[ni][nj] = mat[a][b] + 1
                q.append([ni, nj])


n, m = map(int, input().split()) # n 세로 m 가로
mat = [list(map(int, input().strip())) for _ in range(n)]
vis = [[False] * m for _ in range(n)]
bfs([0,0])
print(mat[n-1][m-1])
