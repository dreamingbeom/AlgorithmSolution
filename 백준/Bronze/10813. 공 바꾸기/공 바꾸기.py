n, m = map(int, input().split())
# n = 바구니 갯수 
# m = 공 바꾸려는 횟수
list_ba = []
for z in range(1, n+1):
    list_ba.append(z)

for y in range(m):
    i, j = map(int, input().split())
    list_ba[i-1], list_ba[j-1] = list_ba[j-1], list_ba[i-1]

print(*list_ba)