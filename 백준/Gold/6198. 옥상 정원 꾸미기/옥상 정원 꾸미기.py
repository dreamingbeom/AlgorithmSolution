import sys
input = sys.stdin.readline
# 메인로직
def main():
    stack = []
    cnt = 0
    for i in range(len(arr)):
        if stack:
            if stack[-1] > arr[i]:
                cnt += len(stack)
                stack.append(arr[i])
            else:
                while stack:
                    if stack[-1] <= arr[i]:
                        stack.pop()
                    else:
                        break
                cnt += len(stack)
                stack.append(arr[i])

        else:
            stack.append(arr[i])
    return cnt



# 인풋

n = int(input()) # 빌딩의 개수
arr = []
for _ in range(n):
    arr.append(int(input()))



# 아웃풋
rul = main()
print(rul)


'''
해당 문제가 스택 문제인지 어떻게 아는가?
어떻게 접근해야하는가?
'''