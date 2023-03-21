T = int(input())
for t in range(T):
    result = ''
    cnt = 0
    for i in range(int(input())):
        a, b = input().split()
        b = int(b)
        if b > cnt:
            result = a
            cnt = b
    print(result)