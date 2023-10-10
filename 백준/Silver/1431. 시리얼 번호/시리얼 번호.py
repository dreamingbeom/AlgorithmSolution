def wow(x):
    cnt = 0
    for i in x:
        if i.isdigit() == True:
            cnt += int(i)
    return cnt

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
arr.sort(key=lambda x:(len(x), wow(x), x))



for i in arr:
    print(i)