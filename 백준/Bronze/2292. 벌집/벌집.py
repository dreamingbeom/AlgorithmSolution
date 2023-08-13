
n = int(input())
i = 1
j = 2
while True:
    if n <= 1 + (6 * i):
        if n == 1:
            print(1)
        else:
            print(j)
        break
    else:
        i += j
        j += 1




