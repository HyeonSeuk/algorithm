a = list(map(int, input().split()))
b = list(map(int, input().split()))

acnt = 0
bcnt = 0
result = 'D'

for i in range(10):
    if a[i] == b[i]:
        acnt += 1
        bcnt += 1
    
    if a[i] > b[i]:
        acnt +=3
        result = 'A'
    
    if a[i] < b[i]:
        bcnt += 3
        result = 'B'
        
if acnt > bcnt:
    print(acnt, bcnt)
    print('A')
elif acnt == bcnt:
        if result == 'A':
            print(acnt, bcnt)
            print('A')
        if result == 'B':
            print(acnt, bcnt)
            print('B')
        if result == 'D':
            print(acnt, bcnt)
            print('D')
else:
    print(acnt, bcnt)
    print('B')