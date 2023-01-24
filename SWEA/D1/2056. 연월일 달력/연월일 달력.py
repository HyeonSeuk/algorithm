lst = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
for t in range(1, int(input())+1):
    a = input()
    year = int(a[0:4])
    month = int(a[4:6])
    day = int(a[6:8])
    result = ''
    if 0 < month < 13 and 0 < day <= lst[month]:
        result = a[0:4]+"/"+a[4:6]+"/"+a[6:8]
    else:
        result = '-1'

    print(f'#{t} {result}') 