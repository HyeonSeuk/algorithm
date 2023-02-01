a, b = map(int, input().split())
card = list(map(int, input().split()))
lst = []
for i in range(0, a-2):
    for j in range(i+1, a-1):
        for k in range(j+1, a):
            if card[i] + card[j] + card[k] <= b:
                lst.append(card[i] + card[j] + card[k])
print(max(lst))