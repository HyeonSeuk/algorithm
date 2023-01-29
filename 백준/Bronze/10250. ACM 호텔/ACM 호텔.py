for t in range(int(input())):
    a, b, c = map(int, input().split())
    ho = c//a
    floor = c%a
    if floor == 0:
        print((a*100)+ho)
    else:
        print((floor*100)+(ho+1))