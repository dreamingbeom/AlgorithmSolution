import sys
input = sys.stdin.readline

k = int(input())
s = []
for i in range(k):
    n = int(input())
    if n != 0:
        s.append(n)
    else:
        if s:
            s.pop()

print(sum(s))

