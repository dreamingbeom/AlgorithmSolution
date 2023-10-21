from collections import deque
import pprint

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
# 메인 로직
def bfs(start):
    q = deque()
    q.append(start)
    distance1[si-1][sj-1] = 0
    distance0[si-1][sj-1] = 0
    while q:
        magic, a, b = q.popleft()
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if mat[ni][nj] == 0:
                    if magic == 1:
                        if distance1[ni][nj] > distance1[a][b] +1:
                            distance1[ni][nj] = distance1[a][b] + 1
                            q.append([1, ni, nj])
                    else:
                        if distance0[ni][nj] > distance0[a][b] +1:
                            distance0[ni][nj] = distance0[a][b] + 1
                            q.append([0, ni, nj])
                else:
                    if magic == 1:
                        if distance0[ni][nj] > distance1[a][b] +1:
                            distance0[ni][nj] = distance1[a][b] + 1
                            q.append([0, ni, nj])
                    else:
                        continue






# 인풋
n , m = map(int, input().split())
#  n은 세로 m 은 가로
si, sj = map(int, input().split())
ei, ej = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
distance1 = [[int(1e9)] * m for _ in range(n)]
distance0 = [[int(1e9)] * m for _ in range(n)]
start = [1, si-1, sj-1]


# 아웃풋
bfs(start)
if distance1[ei-1][ej-1] == int(1e9) and distance0[ei-1][ej-1] == int(1e9):
    print(-1)
else:
    print(min(distance0[ei-1][ej-1], distance1[ei-1][ej-1]))


