def queen(num):
    global cnt
    if num == n:
        cnt += 1
        return

    for j in range(n):
        if vis1[j] == False and vis2[num+j] == False and vis3[j-num+n-1] == False:
            vis1[j] = True
            vis2[num+j] = True
            vis3[j-num+n-1] = True
            queen(num+1)
            vis1[j] = False
            vis2[j+num] = False
            vis3[j-num+n-1] = False



n = int(input())

vis1 = [False] * n # 각 열을 체크
vis2 = [False] * (2 * n - 1) # 대각선체크 abs x+y
vis3 = [False] * (2 * n - 1) # 역대각선 체크 abs x-y
cnt = 0
queen(0)
print(cnt)
