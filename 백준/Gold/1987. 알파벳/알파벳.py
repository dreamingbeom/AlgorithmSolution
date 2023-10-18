import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def dfs(cnt, si, sj):
    global total
    ch.add(mat[si][sj])
    for k in range(4):
        ni = si + di[k]
        nj = sj + dj[k]
        if 0 <= ni < r and 0 <= nj < c:
            if mat[ni][nj] not in ch:
                dfs(cnt+1, ni, nj)
                ch.remove(mat[ni][nj])


    total = max(total, cnt)
    return



# 메인 로직

# 인풋
r, c = map(int, input().split())
# r은 세로 c는 가로
mat = [list(input()) for _ in range(r)]
cnt = 1
total = 0
ch = set()
# 아웃풋

dfs(1, 0, 0)
print(total)

