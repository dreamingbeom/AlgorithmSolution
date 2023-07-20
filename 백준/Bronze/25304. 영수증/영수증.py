X = int(input()) # 영수증에 적힌 총 금액
N = int(input()) # 구매한 물건의 종류 갯수
total = 0
# 내가 계산한 물건과 갯수로 계사한 총 금액
for i in range(1, N+1):
    a, b = map(int, input().split())
    # a는 물건의 가격 b는 물건의 갯수
    total = total + (a * b)

if total == X: # 영수증 금액과 내가 계산한 금액이 맞다면
    print('Yes')
else:
    print(('No'))