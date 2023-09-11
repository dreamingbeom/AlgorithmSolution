import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque()
for i in range(n):
    arr = list(input().split())
    if arr[0] == 'push':
        q.append(arr[1])
    elif arr[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif arr[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif arr[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif arr[0] == 'size':
        print(len(q))
    else:
        if q:
            print(q.popleft())
        else:
            print(-1)


