from collections import deque
import pprint
dz = [0, 0, 0, 0, 1, -1]
di = [-1, 0, 1, 0, 0, 0]
dj = [0, 1, 0, -1, 0, 0]

# 메인로직

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        z , a, b = q.popleft()

        for k in range(6):
            nz = z + dz[k]
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= nz < l and 0 <= ni < r and 0 <= nj < c:
                if vis[nz][ni][nj] == False and mat[nz][ni][nj] != '#':
                    vis[nz][ni][nj] = vis[z][a][b] + 1
                    q.append([nz, ni, nj])


# 인풋

# c개의 문자로 이루어진 r개의 행 l번
# c 층

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    mat = []
    for _ in range(l):
        a = [list(input()) for _ in range(r)]
        mat.append(a)
        trash = input()
    vis = [[[False] * c for _ in range(r)] for _ in range(l)]


    for z in range(l):
        for i in range(r):
            for j in range(c):
                if mat[z][i][j] == 'S':
                    start = [z, i, j]
                    vis[z][i][j] = 0
                elif mat[z][i][j] == 'E':
                    end = [z, i, j]

    bfs(start)
    endz, endi, endj = end
    if vis[endz][endi][endj] != False:
        print(f'Escaped in {vis[endz][endi][endj]} minute(s).')
    else:
        print('Trapped!')

# 아웃풋
