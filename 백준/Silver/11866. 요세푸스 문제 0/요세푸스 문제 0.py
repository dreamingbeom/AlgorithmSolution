from collections import deque

n, k = map(int, input().split())
s = deque()
for i in range(1, n+1):
    s.append(i)

total = []

while s:
    for i in range(k-1):
        s.append(s.popleft())
    total.append(str(s.popleft()))

print('<' + ', '.join(total) + '>')

