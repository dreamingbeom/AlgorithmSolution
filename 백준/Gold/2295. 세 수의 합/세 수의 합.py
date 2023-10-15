def bs(arr, n, key):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return False

# 메인 로직
def main():
    two = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            two.append(arr[i]+arr[j])
    two.sort()
    max_two = 0
    for k in range(len(arr)):
        for l in range(len(arr)):
            ch = bs(two, len(two), arr[l] - arr[k])
            if ch == True:
                max_two = max(max_two, arr[l])
    return max_two




# 인풋
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))



# 아웃풋
rul = main()
print(rul)