import sys
input = sys.stdin.readline
import copy
from collections import deque

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def bfs_j(start):
    q = deque()
    q.append(start)
    while q:
        a , b = q.popleft()
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= ni < r and 0 <= nj < c and mat[ni][nj] == 0:
                mat[ni][nj] = mat[a][b] + 1
                q.append([ni,nj])

def bfs_f(start):
    s = deque()
    for i in range(len(start)):
        s.append(start[i])
    while s:
        z = len(s)
        for j in range(z):
            a, b = s.popleft()
            for k in range(4):
                ni = a + di[k]
                nj = b + dj[k]
                if 0 <= ni < r and 0 <= nj < c and mat_f[ni][nj] == 0:
                    mat_f[ni][nj] = mat_f[a][b] + 1
                    s.append([ni,nj])





r, c = map(int, input().split())
# r= 세로 c = 가로
mat = [list(input().strip()) for _ in range(r)]
mat_f = copy.deepcopy(mat)
ex = []
J = 0
F = []

ch = False
for i in range(c):
    if mat[0][i] == '.':
        ex.append([0,i])
    if mat[0][i] == 'J':
        ch = True
        break
    if mat[r-1][i] == '.':
        ex.append([r-1,i])
    if mat[r-1][i] == 'J':
        ch = True
        break
for i in range(1, r-1):
    if mat[i][0] == '.':
        ex.append([i,0])
    if mat[i][0] == 'J':
        ch = True
        break
    if mat[i][c-1] == '.':
        ex.append([i, c-1])
    if mat[i][c-1] == 'J':
        ch = True
        break
if ch == True:
    print(1)
    exit()


for i in range(r):
    for j in range(c):
        if mat[i][j] == 'J':
            J = [i,j]
            mat[i][j] = 1
            mat_f[i][j] = 0
        elif mat[i][j] == 'F':
            F.append([i,j])
            mat[i][j] = 1
            mat_f[i][j] = 1
        elif mat[i][j] == '#':
            mat[i][j] = -2
            mat_f[i][j] = -2
        else:
            mat[i][j] = 0
            mat_f[i][j] = 0

bfs_j(J)
bfs_f(F)
to = []

for i in ex:
    a, b = i
    if mat[a][b] != 0:
        if mat_f[a][b] != 0:
            if mat[a][b] < mat_f[a][b]:
                to.append(mat[a][b])
        else:
            to.append(mat[a][b])
if len(to) > 0:
        print(min(to))
else:
    print('IMPOSSIBLE')




