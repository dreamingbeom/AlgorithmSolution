n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    ave = i / max(a) * 100
    b.append(ave)

print(sum(b) / n)