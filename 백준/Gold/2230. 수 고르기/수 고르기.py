# 메인 로직
def fun(arr):
    cnt = int(2e9)
    start = 0
    end = 0
    while start <= end  and end < n :
        if m > arr[end] - arr[start]:
            end += 1
        else:
            if cnt >arr[end] - arr[start]:
                cnt = arr[end] - arr[start]
            start += 1

    print(cnt)



# 인풋
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

# 아웃풋
fun(arr)