a = input()
time = 0
for i in a:
    if i in ['A', 'B', 'C']:
        time = time + 3
    elif i in ['D', 'E', 'F']:
        time = time + 4
    elif i in ['G', 'H', 'I']:
        time = time + 5
    elif i in ['J', 'K', 'L']:
        time = time + 6
    elif i in ['M', 'N', 'O']:
        time = time + 7
    elif i in ['P', 'Q', 'R', 'S']:
        time = time + 8
    elif i in ['T', 'U', 'V']:
        time = time + 9
    elif i in ['W', 'X', 'Y', 'Z']:
        time = time + 10
print(time)