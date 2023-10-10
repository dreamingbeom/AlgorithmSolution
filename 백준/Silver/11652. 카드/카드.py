import sys
input = sys.stdin.readline
n = int(input())

dic = {}

for _ in range(n):
    word = int(input())
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
arr = list(dic.items())
arr.sort(key=lambda x:(-x[1], x[0]))
print(arr[0][0])