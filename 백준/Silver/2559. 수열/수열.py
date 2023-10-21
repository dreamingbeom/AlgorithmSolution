
n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(k):
    cnt += arr[i]
total = cnt
for i in range(k, n):
    cnt += arr[i]
    cnt -= arr[i-k]
    total = max(cnt, total )

print(total)