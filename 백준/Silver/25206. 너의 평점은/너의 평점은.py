grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

h = 0
cnt = 0
for i in range(20):
    a, b, c = input().split()
    b = float(b)
    if c != 'P':
        h += b
        cnt += b * grade[c]

print("%.6f" % (cnt / h))