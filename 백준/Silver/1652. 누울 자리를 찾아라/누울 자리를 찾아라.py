a = int(input())
room = [list(input()) for _ in range(a)]
x, y = 0, 0
for i in range(a):
    cnt = 0
    for j in range(a):
        if room[i][j] == '.':
            cnt += 1
            if cnt == 2:
                x += 1
        else:
            cnt = 0
for i in range(a):
    cnt = 0
    for j in range(a):
        if room[j][i] == '.':
            cnt += 1
            if cnt == 2:
                y += 1
        else:
            cnt = 0
print(x, y)