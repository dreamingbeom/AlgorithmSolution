import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    s = []
    ch = 'YES'
    a = list(input().strip())
    for j in range(len(a)):
        if s:
            if a[j] == '(':
                s.append('(')
            else:
                if s:
                    s.pop()
                else:
                    ch = 'NO'
        else:
            if a[j] == '(':
                s.append('(')
            else:
                ch = 'NO'
    if s:
        ch = 'NO'
    print(ch)

