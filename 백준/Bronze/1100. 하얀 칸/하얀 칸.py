import sys
chess = []
cnt = 0
for _ in range(8):
    chess.append(list(map(str,input())))
for i in range(8):
    if i%2 == 0:
        for j in range(0, 8, 2):
            if chess[i][j] == 'F':
                cnt += 1
    else:
        for j in range(1, 8, 2):
            if chess[i][j] == 'F':
                cnt += 1
print(cnt)