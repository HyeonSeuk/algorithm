T = int(input())

for t in range(1, T+1):
    a = input().split(' ')
    for i in a:
        print(i[::-1], end=' ')