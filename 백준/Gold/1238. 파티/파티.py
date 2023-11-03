import heapq
# 메인로직
def go_sor(start, mat, go_map):
    queue = []
    heapq.heappush(queue, [0, start])
    go_map[start] = 0
    while queue:

        cost, node = heapq.heappop(queue)


        if go_map[node] < cost:
            continue

        for next_cost, next_node in mat[node]:

            if go_map[next_node] > go_map[node] + next_cost:
                go_map[next_node] = go_map[node] + next_cost
                heapq.heappush(queue, [go_map[next_node], next_node])


# 인풋

n, m, x = map(int, input().split())

mat = [[] for _ in range(n+1)]
mat_reverse = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, time = map(int, input().split())
    mat[start].append([time, end])
    mat_reverse[end].append([time, start])
go_map = [float('inf')] * (n+1)
back_map = [float('inf')] * (n+1)

max_time = 0
# 아웃풋
go_sor(x, mat, go_map)
go_sor(x, mat_reverse, back_map)



for i in range(1, n+1):
    max_time = max(max_time, go_map[i] + back_map[i])


print(max_time)

