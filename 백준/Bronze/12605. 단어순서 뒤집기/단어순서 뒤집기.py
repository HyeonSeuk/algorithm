for t in range(1, int(input())+1):
    word = list(input().split())
    print(f'Case #{t}:', *word[::-1])