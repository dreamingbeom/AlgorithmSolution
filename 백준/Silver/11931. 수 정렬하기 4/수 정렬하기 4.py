import sys
input = sys.stdin.readline


n = int(input())
cnt = []
for _ in range(n):
    cnt.append(int(input()))

cnt.sort(reverse=True)

for i in range(len(cnt)):
    print(cnt[i])