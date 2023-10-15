# 메인로직
def main():
    stack = []
    rs = [0] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        if stack:
            if stack[-1][0] <= arr[i]:
                while stack:
                    if stack[-1][0] <= arr[i]:
                        a = stack.pop()
                        rs[a[1]] = i+1
                    else:
                        break
                stack.append((arr[i], i))
            else:
                stack.append((arr[i], i))


        else:
            stack.append((arr[i], i))
    return rs



# 인풋
n = int(input())
arr = list(map(int, input().split()))


# 아웃풋
rul = main()
print(*rul)
