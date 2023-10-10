import copy
import sys
input = sys.stdin.readline
di1 = [-1, 0, 1, 0]
dj1 = [0, 1, 0, -1]
di2 = [[0, 0], [-1, 1]]
dj2 = [[-1, 1], [0, 0]]
di3 = [[-1, 0], [0, 1], [1, 0], [0, -1]]
dj3 = [[0,1], [1, 0], [0,-1], [-1, 0]]
di4 = [[0, -1, 0], [-1, 0, 1], [0, 1, 0], [1, 0, -1]]
dj4 = [[-1, 0, 1], [0, 1, 0], [1, 0, -1], [0, -1, 0]]


def fun(depth, mat):
    global cnt
    if depth == len(cctv):
        total = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    total += 1
        if cnt > total:
            cnt = total
        return


    if cctv[depth][0] == 1:
        for k in range(4):
            new_mat = copy.deepcopy(mat)
            i = 1
            while True:
                ni = cctv[depth][1] + (di1[k] * i)
                nj = cctv[depth][2] + (dj1[k] * i)
                if 0 <= ni < n and 0 <= nj < m:
                    if new_mat[ni][nj] == 0:
                        new_mat[ni][nj] = -1
                    elif new_mat[ni][nj] == 6:
                        break
                else:
                    break
                i += 1
            fun(depth + 1, new_mat)


    elif cctv[depth][0] == 2:
        for k in range(2):
            new_mat = copy.deepcopy(mat)
            for l in range(2):
                i = 1
                while True:
                    ni = cctv[depth][1] + (di2[k][l] * i)
                    nj = cctv[depth][2] + (dj2[k][l] * i)
                    if 0 <= ni < n and 0 <= nj < m:
                        if new_mat[ni][nj] == 0:
                            new_mat[ni][nj] = -1
                        elif new_mat[ni][nj] == 6:
                            break
                    else:
                        break
                    i += 1
            fun(depth+1, new_mat)

    elif cctv[depth][0] == 3:
        for k in range(4):
            new_mat = copy.deepcopy(mat)
            for l in range(2):
                i = 1
                while True:
                    ni = cctv[depth][1] + (di3[k][l] * i)
                    nj = cctv[depth][2] + (dj3[k][l] * i)
                    if 0 <= ni < n and 0 <= nj < m:
                        if new_mat[ni][nj] == 0:
                            new_mat[ni][nj] = -1
                        elif new_mat[ni][nj] == 6:
                            break
                    else:
                        break
                    i += 1
            fun(depth + 1, new_mat)
    elif cctv[depth][0] == 4:
        for k in range(4):
            new_mat = copy.deepcopy(mat)
            for l in range(3):
                i = 1
                while True:
                    ni = cctv[depth][1] + (di4[k][l] * i)
                    nj = cctv[depth][2] + (dj4[k][l] * i)
                    if 0 <= ni < n and 0 <= nj < m:
                        if new_mat[ni][nj] == 0:
                            new_mat[ni][nj] = -1
                        elif new_mat[ni][nj] == 6:
                            break
                    else:
                        break
                    i += 1
            fun(depth + 1, new_mat)
    elif cctv[depth][0] == 5:
        new_mat = copy.deepcopy(mat)
        for k in range(4):
            i = 1
            while True:
                ni = cctv[depth][1] + (di1[k] * i)
                nj = cctv[depth][2] + (dj1[k] * i)
                if 0 <= ni < n and 0 <= nj < m:
                    if new_mat[ni][nj] == 0:
                        new_mat[ni][nj] = -1
                    elif new_mat[ni][nj] == 6:
                        break
                else:
                    break
                i += 1
        fun(depth+1, new_mat)



n , m = map(int, input().split())
# n 세로크기 m 가로크기
mat = [list(map(int, input().split())) for _ in range(n)]
cctv = []
for i in range(n):
    for j in range(m):
        if 1 <= mat[i][j] <= 5:
            cctv.append((mat[i][j], i, j))
cnt = n * m
fun(0, mat)
print(cnt)