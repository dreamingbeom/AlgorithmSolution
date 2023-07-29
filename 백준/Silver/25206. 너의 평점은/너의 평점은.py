
dict = {'A+': 4.5,
        'A0':4.0,
        'B+':3.5,
        'B0':3.0,
        'C+':2.5,
        'C0':2.0,
        'D+':1.5,
        'D0':1.0,
        'F': 0.0}
b = []
d = []
for i in range(20):
        a = list((input().split()))
        if 'P' not in a[2]:
            a.insert(2, dict[a[2]])
            c = float(a[1]) * float(a[2])
            b.append(c)
            d.append(float(a[1]))
print(sum(b) / sum(d))