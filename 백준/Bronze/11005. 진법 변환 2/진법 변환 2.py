
n, m = map(int, input().split())
a = ''
while n:

    if 35 >= n % m >= 10:
        a += chr((n % m)+55)
    else:
        a += str(n % m)
    n //= m

print(a[::-1])