import sys
input = sys.stdin.readline
n = int(input())

mat = [list(input().split()) for _ in range(n)]
for i in range(n):
    mat[i][0] = int(mat[i][0])
mat.sort(key =lambda x:x[0])
for i in mat:
    print(*i)