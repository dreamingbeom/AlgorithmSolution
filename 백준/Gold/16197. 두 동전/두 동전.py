from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 메인로직
def sor(coin):
    queue = deque()
    queue.append(coin)

    total = 99999
    while queue:
        coin1, coin2, cnt = queue.popleft()

        if cnt == 10:
            total = -2
            return

        a, b = coin1
        c, d = coin2

        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            ci = c + di[k]
            cj = d + dj[k]
            coin_one = [a, b]
            coin_two = [c, d]
            if (0 <= ni < n and 0 <= nj < m) or (0 <= ci <= n and 0 <= cj < m):
            # 만약 코인1과 코인 2중에서 하나라도 안나가고 이동한다면
                if (0 <= ni < n and 0 <= nj < m) and (0 <= ci < n and 0 <= cj < m) :
                # 그중에서 코인1이랑 코인2 둘다 내부에있다면
                    if mat[ni][nj] != '#':
                    # 만약 코인1이 벽을 안만난다면
                        coin_one = [ni, nj]
                        # 다음 코인1 좌표 갱신
                    if mat[ci][cj] != '#':
                    # 만약 코인2이 벽을 안만난다면
                        coin_two = [ci, cj]
                        # 다음 코인2 좌표 갱신
                elif (0 <= ni < n and 0 <= nj < m) and (ci < 0 or cj < 0 or ci >=n or cj >= m):
                # 만약 코인1은 내부인데 코인2는 튕겨 나가는 중이라면
                    total = min(total, cnt)
                    return total
                    # 기존 최저값과 팅겨져 나갔을 때의 비교해서 갱신
                elif (0 <= ci < n and 0 <= cj < m) and (ni < 0 or nj <0 or ni >= n or nj >= m):
                # 만약 코인2은 내부인데 코인1은 팅겨져 나간다면
                    total = min(total, cnt)
                    return total
                    # 기존 최저값과 팅겨져 나갔을 때의 횟수 비교갱신
                queue.append([coin_one, coin_two, cnt+1])
                # 일단 뭐라도 내부에 있었으니 좌표 queue에 넣기 횟수 +1 해서!

            elif (ni < 0 or nj <0 or ni >= n or nj >= m) and (ci < 0 or cj < 0 or ci >=n or cj >= m):
                # 만약 둘다 나가리라면?
                continue
                # 둘다 나가는건 안되니까 패스
    return total

# 인풋

n, m = map(int, input().split())
mat = [list(input()) for _ in range(n)]


coin = []
for i in range(n):
    for j in range(m):
        if mat[i][j] == 'o':
            coin.append([i,j])
coin.append(0)

rs = sor(coin)


# 아웃풋
if rs == None:
    print(-1)
else:
    print(rs+1)




