# import sys
# input = sys.stdin.readline
from collections import deque
import copy

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs1(start):
    global cnt1
    q = deque()
    q.append(start)
    while q:
        a, b = q.popleft()
        vis1[a][b] = True
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if vis1[ni][nj] == False and mat[ni][nj] == 'R':
                    vis1[ni][nj] = True
                    q.append([ni, nj])
    cnt1 += 1

def bfs2(start):
    global cnt2
    q = deque()
    q.append(start)
    while q:
        a, b = q.popleft()
        vis1[a][b] = True
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if vis1[ni][nj] == False and mat[ni][nj] == 'B':
                    vis1[ni][nj] = True
                    q.append([ni, nj])
    cnt2 += 1

def bfs3(start):
    global cnt3
    q = deque()
    q.append(start)
    while q:
        a, b = q.popleft()
        vis1[a][b] = True
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if vis1[ni][nj] == False and mat[ni][nj] == 'G':
                    vis1[ni][nj] = True
                    q.append([ni, nj])
    cnt3 += 1


def bfs4(start):
    global cnt4
    q = deque()
    q.append(start)
    while q:
        a, b = q.popleft()
        vis2[a][b] = True
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if vis2[ni][nj] == False:
                    if mat[ni][nj] == 'G' or mat[ni][nj] == 'R':
                        vis2[ni][nj] = True
                        q.append([ni, nj])
    cnt4 += 1


n = int(input())
mat = [list(input()) for _ in range(n)]
vis1 = [[False] * n for _ in range(n)] # 레드 블루 그린
vis2 = [[False] * n for _ in range(n)] # 레드 + 그린
cnt1 = 0 # 레드
cnt2 = 0 # blue
cnt3 = 0 # green
cnt4 = 0 # red + green

for i in range(n):
    for j in range(n):
        if mat[i][j] == 'R':
            if vis1[i][j] == False:
                bfs1([i, j])
            if vis2[i][j] == False:
                bfs4([i, j])
        elif mat[i][j] == 'B':
            if vis1[i][j] == False:
                bfs2([i, j])
        else:
            if vis1[i][j] == False:
                bfs3([i,j])
            if vis2[i][j] == False:
                bfs4([i,j])

print(cnt1+cnt2+cnt3, cnt4+cnt2)






