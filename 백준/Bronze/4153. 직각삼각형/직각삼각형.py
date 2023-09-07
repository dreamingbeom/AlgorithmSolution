while True:
    n = list(map(int, input().split()))
    if n == [0, 0, 0]:
        break
    ans = 'wrong'
    if (n[0]**2) + (n[1]**2) == n[2]**2:
        ans = 'right'
    if (n[0]**2) + (n[2]**2) == n[1]**2:
        ans = 'right'
    if (n[1]**2) + (n[2]**2) == n[0]**2:
        ans = 'right'

    print(ans)
