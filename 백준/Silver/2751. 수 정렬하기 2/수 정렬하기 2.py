import sys
lst = []
for _ in range(int(input())):
    lst.append(int(sys.stdin.readline()))
lst.sort()

for i in lst:
    print(i)