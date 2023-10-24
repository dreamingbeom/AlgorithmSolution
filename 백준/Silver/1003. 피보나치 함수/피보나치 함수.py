t = int(input())

for tc in range(t):
    n = int(input())
    arr = [[0, 0] for _ in range(41)]
    arr[0][0] = 1
    arr[1][1] = 1
    arr[2][0] = 1
    arr[2][1] = 1
    if n >= 3:
        for i in range(3, 41):
            arr[i][0] = arr[i-1][0] + arr[i-2][0]
            arr[i][1] = arr[i-1][1] + arr[i-2][1]
    print(arr[n][0], end=' ')
    print(arr[n][1])