for t in range(1, int(input())+1):
    a = input()
    if a == a[::-1]:
        print(f'#{t}', 1)
    else:
        print(f'#{t}', 0)