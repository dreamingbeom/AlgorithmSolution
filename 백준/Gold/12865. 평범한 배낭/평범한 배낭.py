n, k = map(int, input().split())

arr = [[0,0]]
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])

mat = [[0] * (k +1) for _ in range(n+1)]

for j in range(1, k+1):
    for i in range(1, n+1):
        if arr[i][0] > j:
            mat[i][j] = mat[i-1][j]
        else:
            mat[i][j] = max(mat[i-1][j], arr[i][1]+mat[i-1][j-arr[i][0]])

print(mat[n][k])


