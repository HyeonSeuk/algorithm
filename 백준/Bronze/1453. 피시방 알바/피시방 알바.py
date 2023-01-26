lst = []
person = int(input())
want = list(map(int, input().split()))
n = 0
for i in range(person):
    if want[i] in lst:
        n += 1
    else:
        lst.append(want[i])
print(n)