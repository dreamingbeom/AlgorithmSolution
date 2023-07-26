c = []
b = 0
for i in range(10):
    a = int(input())
    b = a % 42
    if b not in c:
        c.append(b)

print(len(c))