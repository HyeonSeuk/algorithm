a = input().upper()
a_lst = list(set(a))

lst = []
for i in a_lst:
    cnt = a.count
    lst.append(cnt(i))
if lst.count(max(lst)) > 1:
    print('?')
else:
    print(a_lst[(lst.index(max(lst)))])