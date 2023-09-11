# import sys
# input = sys.stdin.readline
from collections import deque
n , m = map(int, input().split())
arr = list(map(int, input().split()))
mat = deque(i for i in range(1, n+1))
cnt = 0
for j in range(m):
    mid = len(mat) / 2
    h = 0
    a = mat.index(arr[j])
    if mat.index(arr[j]) >= mid:
        while True:
            if mat[h] == arr[j]:
                mat.popleft()
                break
            else:
                mat.appendleft(mat.pop())
                cnt += 1
                h += 0
    else:
        while True:
            if mat[h] == arr[j]:
                mat.popleft()
                break
            else:
                mat.append(mat.popleft())
                cnt += 1
                h += 0
print(cnt)