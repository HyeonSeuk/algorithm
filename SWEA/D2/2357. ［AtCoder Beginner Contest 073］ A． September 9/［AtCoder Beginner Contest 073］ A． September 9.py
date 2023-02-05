for t in range(1, int(input())+1):
    n = list(input())
    cnt =0
    for i in n:
        if i == '9':
            cnt += 2
        else:
            cnt -= 1
    if cnt >= 1:
        print(f'#{t} Yes')
    elif 0 > cnt:
        print(f'#{t} No')