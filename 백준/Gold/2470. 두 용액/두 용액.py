# 메인로직
def bs(key, i):
    start = i + 1
    end = len(arr) - 1
    cnt = i+1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] + key == 0:
            cnt = mid
            return cnt
        elif abs(arr[mid] + key) > 0:
            if arr[mid] + key < 0:
                start = mid + 1
                if abs(arr[cnt] + key) > abs(arr[mid] + key):
                    cnt = mid
            elif arr[mid] + key > 0:
                end = mid - 1
                if abs(arr[cnt] + key) > abs(arr[mid] + key):
                    cnt = mid
    return cnt


def fun():
    total = []
    for i in range(len(arr)-1):
        key = arr[i]
        cnt = bs(key, i) # arr[i]가 가질 수 있는 두 수의 합중 최소값을 가진 다른 수
        total.append([arr[cnt] + key, key, arr[cnt]])
    total.sort(key=lambda x:abs(x[0]))
    print(total[0][1], end=' ')
    print(total[0][2])



# 인풋
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

# 아웃풋
fun()