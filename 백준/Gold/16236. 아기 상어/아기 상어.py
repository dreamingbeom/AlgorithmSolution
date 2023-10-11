from collections import deque

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def bfs(start):
    global shark_lv
    distince = [[0] * n for _ in range(n)]
    q = deque()
    q.append(start)
    fish = []
    while q:
        a, b = q.popleft()
        vis[a][b] = True
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= ni < n and 0 <= nj < n and vis[ni][nj] == False:
                if mat[ni][nj] <= shark_lv:
                    vis[ni][nj] = True
                    distince[ni][nj] = distince[a][b] + 1
                    q.append((ni,nj))
                    if mat[ni][nj] < shark_lv and mat[ni][nj] != 0:
                        fish.append((distince[ni][nj], ni, nj))
    fish.sort(key=lambda x: (x[0], x[1], x[2]))
    return distince, fish




n = int(input()) # 공간 크기 N* N
mat = [list(map(int, input().split())) for _ in range(n)]
shark_lv = 2
shark_exr = 0
second = 0
start = []
for i in range(n):
    for j in range(n):
        if mat[i][j] == 9:
            start = (i, j)
            mat[i][j] = 0

while True:

    if shark_lv == shark_exr:
        shark_lv += 1
        shark_exr = 0
    vis = [[False] * n for _ in range(n)]
    dis, fish = bfs(start)
    if len(fish) > 0:
        fish_dis, fish_i, fish_j = fish[0]
        start = (fish_i, fish_j)
        second += fish_dis
        shark_exr += 1
        mat[fish_i][fish_j] = 0

    else:
        break
print(second)



