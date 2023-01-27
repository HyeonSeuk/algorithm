s = input()
n = 0
while True:
    q = input()
    if q == '고무오리 디버깅 끝':
        break
    else:
        if q == '문제':
            n += 1
        elif q == '고무오리':
            if n == 0:
                n += 2
            else:
                n -= 1
if n == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')