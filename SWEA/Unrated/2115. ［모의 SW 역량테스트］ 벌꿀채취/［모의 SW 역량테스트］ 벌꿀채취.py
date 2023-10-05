def bubun(depth, bvis, cnt_total , cnt):
    if depth == m:
        total = [cnt[i] for i in range(len(bvis)) if bvis[i] == True]
        if sum(total) <= c and len(total) >= 1:
            cnt_total.append(total)
        return

    bvis[depth] = True
    bubun(depth + 1, bvis, cnt_total, cnt)

    bvis[depth] = False
    bubun(depth + 1, bvis, cnt_total, cnt)


t = int(input())

for tc in range(1, t + 1):
    n, m, c = map(int, input().split())
    # n = 벌통 가로 세로 크기 , m = 선택 할 수 있는 벌통의 개수 c = 최대 채취 양
    mat = [list(map(int, input().split())) for _ in range(n)]
    vis = [[False] * n for _ in range(n)]
    real_total = []
    for i in range(n):
        for j in range(n - m + 1):
            cnt_j = []
            for y in range(m):
                nj = j + y
                cnt_j.append(mat[i][nj])
                vis[i][nj] = True
            buvis = [False] * m
            cnt_j_total = []
            bubun(0, buvis, cnt_j_total, cnt_j)
            cnt_j_max = []
            for e in range(len(cnt_j_total)):
                cnt_j_total_list = []
                for r in range(len(cnt_j_total[e])):
                    cnt_j_total_list.append(cnt_j_total[e][r] ** 2)
                    cnt_j_max.append(sum(cnt_j_total_list))
            cnt_total_j_max = max(cnt_j_max)
            cnt_real_total_q = []
            for p in range(n):
                for q in range(n - m + 1):
                    cnt_q = []
                    for k in range(m):
                        nq = q + k
                        if vis[p][nq] == False:
                            cnt_q.append(mat[p][nq])
                    if len(cnt_q) != m:
                        continue
                    bubuvis = [False] * m
                    cnt_q_total = []
                    bubun(0, bubuvis, cnt_q_total, cnt_q)
                    cnt_q_max = []
                    for u in range(len(cnt_q_total)):
                        cnt_q_total_list = []
                        for o in range(len(cnt_q_total[u])):
                            cnt_q_total_list.append(cnt_q_total[u][o] ** 2)
                            cnt_q_max.append(sum(cnt_q_total_list))
                    cnt_total_q_max = max(cnt_q_max)
                    cnt_real_total_q.append(cnt_total_q_max)
            for f in range(m):
                nj = j + f
                vis[i][nj] = False
            real_total.append(cnt_total_j_max + max(cnt_real_total_q))
    print(f'#{tc} {max(real_total)}')
