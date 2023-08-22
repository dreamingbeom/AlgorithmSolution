n = int(input())
n_list = []
for i in range(666, 10000000):
    if '666' in str(i):
        n_list.append(i)

n_list.sort()

print(n_list[n-1])
