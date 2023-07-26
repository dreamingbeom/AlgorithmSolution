n , m = map(int, input().split())
# n은 바구니의 개수
# m은 돌리는 횟수
a = []
for i in range(1, n+1):
    a.append(i)

for x in range(m):
    i, j = map(int, input().split())
    if i  == 1:
        b = a[j-1:None:-1]
        a[0:j] = b
    elif i != 1:
        b = a[j-1:i-2:-1]
        a[i-1:j] = b
print(*a)