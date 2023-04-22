n = int(input())
if n % 5 == 0:
    print(n // 5)
else:
    cnt = n // 5
    while cnt >= 0:
        if (n - cnt * 5) % 3 == 0:
            print(cnt + (n - cnt * 5) // 3)
            break
        cnt -= 1
    else:
        print(-1)