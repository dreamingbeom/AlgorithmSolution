# 메인 로직

def sor():
    cnt = 1
    end = schedule[0][1]
    for i in range(1, n):
        if schedule[i][0] >= end:
            cnt += 1
            end = schedule[i][1]
    return cnt







# 인풋
n = int(input())
schedule = []
for _ in range(n):
    start_time, end_time = map(int, input().split())
    schedule.append([start_time, end_time])

schedule.sort(key= lambda x:(x[1],x[0] ,x[1]-x[0]))


# 아웃풋
rs = sor()
print(rs)

