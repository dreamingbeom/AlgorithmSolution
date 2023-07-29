n = int(input())

for i in range(n):
    b = input()
    for i in range(1, len(b)):
        if b[i-1] == b[i]:
            continue
        elif b[i-1] in b[i+1:]:
                n = n-1
                break


print(n)