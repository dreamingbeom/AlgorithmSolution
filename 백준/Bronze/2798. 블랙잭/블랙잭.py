n, m = map(int, input().split()) # n은 카드개수 m은 만들숫자
card = list(map(int, input().split()))
ans = []
# card 집합에서 3장의 카드를 뽑아 더하고 이를 새 리스트에 담는다
# 새 리스트에 각 값을 -21을 해주고 그 절댓값중 가장 작은 값을 반환한다

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if card[i]+card[j]+card[k] <= m:
                ans.append((card[i] + card[j] + card[k]))

print(max(ans))

