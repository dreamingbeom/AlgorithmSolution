import sys
input = sys.stdin.readline
from collections import deque


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def bfs(start):
    q = deque()
    q.append(start)
    global cnt
    while q:
        a, b = q.popleft()
        vis[a][b] = True
        for z in range(4):
            ni = a + di[z]
            nj = b + dj[z]
            if 0 <= ni < n and 0 <= nj < m and mat[ni][nj] == 1 and vis[ni][nj] == False:
                vis[ni][nj] = True
                q.append([ni, nj])
    cnt += 1

t = int(input())

for tc in range(t):
    m, n, k = map(int, input().split())
    mat = [[0] * m for _ in range(n)]
    vis = [[False] * m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        c = list(map(int, input().split()))
        mat[c[1]][c[0]] = 1

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1 and vis[i][j] == False:
                bfs([i, j])

    print(cnt)

