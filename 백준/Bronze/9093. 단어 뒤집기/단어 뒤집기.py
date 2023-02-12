for t in range(int(input())):
    word = list(input().split())
    for i in word:
        a = i[::-1]
        print(a, end= ' ')