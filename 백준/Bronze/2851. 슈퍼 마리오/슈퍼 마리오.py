lst = []
cnt1 = 0
cnt2 = 0
for i in range(10):
    lst.append(int(input()))
for i in lst:
    cnt1 += i
    if cnt1 >= 100:
        cnt2 = cnt1 - i
        break
if cnt1 - 100 > 100 - cnt2:
    print(cnt2)
elif cnt1 - 100 == 100 - cnt2:
    print(max(cnt1, cnt2))
else:
    print(cnt1)