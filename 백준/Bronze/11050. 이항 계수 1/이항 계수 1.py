n, r = map(int, input().split())
nn = 1
rr = 1
rn = 1
for i in range(1, n+1):
    nn = nn * i
for i in range(1, r+1):
    rr = rr * i
for i in range(1, n-r+1):
    rn = rn * i

print(int(nn / (rr * rn)))