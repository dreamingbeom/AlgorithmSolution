
import sys
input = sys.stdin.readline

n = int(input())

mat = [list(map(int, input().split())) for _ in range(n)]
b = sorted(mat ,key=lambda x:(x[1], x[0]))

for i in b:
    print(*i)