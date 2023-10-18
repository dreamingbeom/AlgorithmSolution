import heapq

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs(start):
    q = []
    heapq.heappush(q, start)
    vis[0][0] = 0
    while q:
        c, a, b = heapq.heappop(q)
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if vis[ni][nj] > c:
                    if mat[ni][nj] == 1:
                        vis[ni][nj] = c
                        heapq.heappush(q, (vis[ni][nj], ni, nj))
                    else:
                        vis[ni][nj] = c + 1
                        heapq.heappush(q, (vis[ni][nj], ni, nj))
    return vis[n-1][n-1]


# 메인
def main():
    pass


# 인풋
n = int(input())
mat = [list(map(int, input())) for _ in range(n)]
vis = [[9999] * n for _ in range(n)]
start = [0,0,0] # 비용 , i, j



# 아웃풋
rs = bfs(start)
print(rs)
