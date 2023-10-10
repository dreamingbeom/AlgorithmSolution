import sys
input = sys.stdin.readline

n = int(input())
b = []
for _ in range(n):
    a = int(input())
    b.append(a)

b.sort()
for i in range(n):
    print(b[i])
