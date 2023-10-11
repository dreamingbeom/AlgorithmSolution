from collections import deque
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(shark):
    q = deque()
    for i in shark:
        q.append(i)
    while q:
        a, b = q.popleft()
        for k in range(8):
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= ni < n and 0 <= nj < m and vis[ni][nj] == False:
                vis[ni][nj] = True
                if mat[a][b] == -1:
                    mat[ni][nj] = 1
                else:
                    mat[ni][nj] = mat[a][b] + 1
                q.append((ni,nj))


n, m = map(int, input().split())
# n은 세로 m은 가로
mat = [list(map(int, input().split())) for _ in range(n)]
vis = [[False] * m for _ in range(n)]
shark = []
cnt = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] == 1:
            shark.append((i,j))
            mat[i][j] = -1
            vis[i][j] = True

bfs(shark)
for i in range(n):
    for j in range(m):
        cnt = max(cnt, mat[i][j])
print(cnt)

