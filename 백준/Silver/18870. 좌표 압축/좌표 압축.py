n = int(input())
arr = list(map(int, input().split()))

new = list(set(arr))
new.sort()
dic = {}

for i in range(len(new)):
    dic[new[i]] = i

for j in range(len(arr)):
    arr[j] = dic[arr[j]]


print(*arr)
