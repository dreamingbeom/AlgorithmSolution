a = list(input().upper())

alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
        'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']
b = []

for i in alph:
    c = a.count(i)
    if c > 0:
        b.append(c)
    else:
        b.append(0)

if b.count(max(b)) >=2:
    print('?')
else:
    alph_index = b.index(max(b))
    print(alph[alph_index])









