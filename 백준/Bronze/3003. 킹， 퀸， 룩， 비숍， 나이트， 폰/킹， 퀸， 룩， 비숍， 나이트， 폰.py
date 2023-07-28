
origin = [1, 1, 2, 2, 2, 8]

two = list(map(int, input().split()))
new = []
for i in range(len(two)):
    a = origin[i] - two[i]
    new.append(a)

print(*new)