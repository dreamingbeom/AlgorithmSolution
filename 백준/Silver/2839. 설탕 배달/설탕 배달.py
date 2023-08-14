n = int(input())
sugar = []

for i in range((n//3)+1):
    for j in range((n//3)+1):
        if (3*i) + (5*j) == n:
            sugar.append(i+j)

if len(sugar) == 0:
    print(-1)
else:
    print(min(sugar))

