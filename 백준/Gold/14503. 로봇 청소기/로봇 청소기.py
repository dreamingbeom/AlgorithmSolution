

# 메인로직

def sim(r, c, d):
    global cnt
    while True:
        if mat[r][c] == 0:
            cnt += 1
            mat[r][c] = 2

        for k in range(1, 5):
            di, dj = direction[(d-k)%4]
            ni = r + di
            nj = c + dj
            if 0 <= ni < n and 0 <= nj < m and mat[ni][nj] == 0:
                d = (d-k)%4
                r = ni
                c = nj
                break
        else:
            ni, nj = direction[(d-2)%4]
            if mat[r+ni][c+nj] == 1:
                return
            else:
                r += ni
                c += nj






# 인풋
n, m = map(int, input().split())
# n 세로 m 가로
r, c, d = map(int, input().split())
# 시작좌표 (r, c)  바라보는 방향 d
# 0 북쪽 1 동쪽 2 남쪽 3 서쪽
mat = [list(map(int, input().split())) for _ in range(n)]
vis = [[False] * m for _ in range(n)]
cnt = 0
direction = [(-1,0), (0, 1), (1,0), (0,-1)]
# 아웃풋
sim(r, c, d)
print(cnt)