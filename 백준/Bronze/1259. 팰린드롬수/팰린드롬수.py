
while True:
    n = list(input())
    if '0' == n[0]:
        break
    rn = n[::-1]
    ans = 'yes'
    for i in range(len(n)):
        if n[i] != rn[i]:
            ans = 'no'
            break
    print(ans)
