
def fun(depth):
    if depth == m:
        print(*total)
        return

    for i in range(1, n+1):
        if arr[i] == False:
            arr[i] = True
            total.append(i)
            fun(depth+1)
            arr[i] = False
            total.pop()


n, m = map(int, input().split())
arr = [False] * (n+1)
total = []
fun(0)

