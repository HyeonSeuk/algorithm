a = input()
lst = []
for i in range(1, len(a)):
    for j in range(i+1, len(a)):
        first = a[:i][::-1]
        second = a[i:j][::-1]
        third = a[j:][::-1]
        lst.append(first + second + third)
lst.sort()
print(lst[0])