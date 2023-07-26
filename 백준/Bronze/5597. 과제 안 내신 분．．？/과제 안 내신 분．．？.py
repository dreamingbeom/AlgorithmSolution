
# n = 바구니 갯수 
# m = 공 바꾸려는 횟수
list_ba = []
for z in range(1, 30+1):
    list_ba.append(z)

for y in range(1, 29):
    a = int(input())
    list_ba[a-1] = 0

list_ba.sort()

print(list_ba[-2])
print(list_ba[-1])