

# 메인로직
def main():
    start = 1
    end = max(arr)
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in range(len(arr)):
            cnt += (arr[i] // mid )
        if cnt >= n:
            start = mid + 1
        else:
            end = mid - 1
    return end

# 인풋
k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))



# 아웃풋
rs = main()
print(rs)
