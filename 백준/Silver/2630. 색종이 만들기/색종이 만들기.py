import pprint
# 메인로직
def fun(i_start, j_start, n):
    global cnt_blue
    global cnt_white
    if n == 1:
        if mat[i_start][j_start] == 1:
            cnt_blue += 1
        else:
            cnt_white += 1
        return

    ch_blue = False
    ch_white = False
    for i in range(i_start, i_start+n):
        for j in range(j_start, j_start+n):
            if mat[i][j] == 1:
                ch_blue= True
            elif mat[i][j] == 0:
                ch_white = True
    if ch_blue == True and ch_white == True:
            fun(i_start, j_start, n//2)
            fun(i_start, j_start+(n//2), n//2)
            fun(i_start+(n//2), j_start, n//2)
            fun(i_start+(n//2), j_start+(n//2), n//2)

    else:
        if ch_blue == True and ch_white == False:
            cnt_blue += 1
        elif ch_blue == False and ch_white == True:
            cnt_white += 1
        return


# 인풋
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
cnt_blue = 0
cnt_white = 0
fun(0, 0, n)

# 아웃풋
print(cnt_white)
print(cnt_blue)
