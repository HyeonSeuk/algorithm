import sys
lst = []
for i in range(int(sys.stdin.readline())):
    lst.append(sys.stdin.readline().strip())
lst_set = list(set(lst))
lst_set.sort()
print(*sorted(lst_set, key=len),sep='\n')