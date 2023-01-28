for t in range(int(input())):
    a = list(map(int, input().split()))
    avg = sum(a[1:])/a[0]
    n = 0
    for i in range(1, len(a)):
        if a[i] > avg:
            n += 1
    print('%.3f' % (n / a[0] * 100) + '%')