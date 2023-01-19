company = {}
for t in range(int(input())):
    Key, Value = input().split()
    if Value == 'enter':
        company[Key] = True
    else:
        del(company[Key])

for Key in sorted(company.keys(), reverse=True):
    print(Key)