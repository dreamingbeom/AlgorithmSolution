import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    command = input().strip()
    n = int(input())
    arr = deque(input().strip('[]\n').split(','))
    ch = True
    error = True
    if n == 0:
        arr = []

        if 'D' in command:
            print('error')
            continue
        else:
            print('[]')
            continue

    for i in command:
        if i == 'R':
            if ch == True:
                ch = False
            else:
                ch = True
        elif i == 'D':
            if arr:
                if ch == True:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                error = False
                break

    if ch == False:
        arr.reverse()

    if arr:
        s = []
        for i in arr:
            s.append(i)
        print('[' + ','.join(s) + ']')
    else:
        if error == True:
            print('[]')
        else:
            print('error')
