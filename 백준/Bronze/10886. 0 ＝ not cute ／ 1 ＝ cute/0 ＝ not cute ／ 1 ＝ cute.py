p = int(input())
yes = 0
no = 0
for i in range(p):
    a = int(input())
    if a == 0:
        no += 1
    elif a == 1:
        yes += 1
if no > yes:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')