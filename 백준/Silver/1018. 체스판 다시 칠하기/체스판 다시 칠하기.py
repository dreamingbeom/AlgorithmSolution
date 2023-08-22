
n, m = map(int, input().split())
mat = [list(input()) for _ in range(n)]
total = []
ans_B = [['B','W','B','W','B','W','B','W'], ['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'], ['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'], ['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'], ['W','B','W','B','W','B','W','B']]
ans_W = [['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]


# 맨위가 화이트
for i in range(n-7):
    for j in range(m-7):
        cnt = 0
        for p in range(8):
            for q in range(8):
                if mat[i+p][j+q] != ans_W[p][q]:
                    cnt += 1
        total.append(cnt)
# 맨위가 블랙
# 맨위가 화이트
for i in range(n-7):
    for j in range(m-7):
        cnt = 0
        for p in range(8):
            for q in range(8):
                if mat[i + p][j + q] != ans_B[p][q]:
                    cnt += 1
        total.append(cnt)

print(min(total))