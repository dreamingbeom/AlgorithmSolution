# 메인 로직

# 인풋
n, s = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = [0]
cnt = 0
for i in range(len(arr)):
    cnt += arr[i]
    arr2.append(cnt)
start = 0
end = 0
total = int(1e10)

for i in arr:
    if i >= s:
        total = 1
        break

while start <= end and end < n+1:
    if s <= arr2[end] - arr2[start]:
        if total > end - start:
            total = end - start
        start += 1
    else:
        end += 1

if total != int(1e10):
    print(total)
else:
    print(0)



# 아웃풋
