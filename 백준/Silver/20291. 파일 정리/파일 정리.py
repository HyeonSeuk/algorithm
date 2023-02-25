import sys
input = sys.stdin.readline

file = {}
for i in range(int(input())):
    a = input().split()[0].split('.')[1]
    if a in file:
        file[a] += 1
    else:
        file[a] = 1
for value in sorted(file.items()):
    print(value[0], value[1])