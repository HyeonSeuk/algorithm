from collections import Counter
lst = []
for i in range(10):
    a = int(input())
    lst.append(a)
counter = Counter(lst)
most = counter.most_common(2)
print(sum((lst))//10)
print(most[0][0])