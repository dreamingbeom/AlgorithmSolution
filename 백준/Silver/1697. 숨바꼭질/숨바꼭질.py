from collections import deque

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        a = q.popleft()
        ni = a + 1
        if 0 <= ni < 100001 and arr[ni] == 0:
            arr[ni] = arr[a] + 1
            q.append(ni)
        ni = a - 1
        if 0 <= ni < 100001 and arr[ni] == 0:
            arr[ni] = arr[a] + 1
            q.append(ni)
        ni = a * 2
        if 0 <= ni < 100001 and arr[ni] == 0:
            arr[ni] = arr[a] + 1
            q.append(ni)


n, m = map(int, input().split())

arr = [0] * 100001

arr[n] = 1 # 시작점

bfs(n)
print(arr[m]-1)


