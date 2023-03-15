T = int(input())
lst = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
for t in range(1, T+1):
    n = input()
    if n == 'SUN':
        print(f'#{t} {7}')
    else:
        print(f'#{t} {6 - lst.index(n)}')