import sys
input = sys.stdin.readline

def push(n):
    s.append(n)

def poping():
    if len(s) >= 1:
        a = s.pop()
        print(a)
    else:
        print(-1)

def size():
    a = len(s)
    print(a)
def empty():
    if len(s) >= 1:
        print(0)
    else:
        print(1)
def top():
    if len(s) >= 1:
        print(s[-1])
    else:
        print(-1)

n = int(input())
s = []
for i in range(n):
    ming = list(input().strip().split())
    if ming[0] == 'push':
        push(int(ming[1]))
    elif ming[0] == 'pop':
        poping()
    elif ming[0] == 'size':
        size()
    elif ming[0] == 'empty':
        empty()
    elif ming[0] == 'top':
        top()