a, b = input().split()

min_list = []

for i in range(len(b)-len(a)+1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt += 1
    min_list.append(cnt)
print(min(min_list))


