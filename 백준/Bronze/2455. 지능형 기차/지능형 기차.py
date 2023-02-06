max_p = 0
lst = []
for i in range(4):
    out_p, in_p = map(int, input().split())
    max_p += in_p
    max_p -= out_p
    lst.append(max_p)
print(max(lst))