n, m = map(int, input().split())
# n = 바구니 갯수 
# m = 시도 횟수
list_ba = []
for z in range(n):
    list_ba.append(0)

for x in range(m):
    i, j, k = map(int, input().split())
    list_ba[(i-1):(j)] = [k] * (j-(i-1))

for y in list_ba:
    print(y, end=' ')
    # i번 바구니부터 j번 바구니까지 k번 적혀있는 공을 넣겠다