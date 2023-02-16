from collections import Counter

lst = []
for i in range(int(input())):
    lst.append(input())

lst.sort()
counter = Counter(lst)
most_common = counter.most_common(2)

print(most_common[0][0])