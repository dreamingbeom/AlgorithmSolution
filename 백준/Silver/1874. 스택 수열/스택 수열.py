import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = deque(i for i in range(1, n+1))
s = []
ans = []

for i in range(n):
    x = int(input())
    if x not in s:
        while True:
            a = arr.popleft()
            s.append(a)
            ans.append('+')
            if a == x:
                s.pop()
                ans.append('-')
                break
    else:
        if s[-1] == x:
            s.pop()
            ans.append('-')
        else:
            ans.append('NO')
if 'NO' in ans:
    print('NO')
else:
    for i in ans:
        print(i)


