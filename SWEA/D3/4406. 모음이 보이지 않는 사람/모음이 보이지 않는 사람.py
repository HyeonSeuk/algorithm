for t in range(1, int(input())+1):
    a = input()
    word = 'aeiou'
    result = ''
    for i in a:
        if i not in word:
            result += i
    print(f'#{t} {result}')