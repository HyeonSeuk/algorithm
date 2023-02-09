for t in range(1, int(input())+1):
    a = int(input())
    card = list(input().split())
    d = len(card)//2
    card1 = []
    card2 = []
    if len(card)%2 == 1:
        for i in range(d+1):
            card1.append(card[i])
        else:
            for j in range(d):
                card2.append(card[j+d+1])
    else:
        if len(card)%2 == 0:
            for k in range(d):
                card1.append(card[k])
            else:
                for l in range(d):
                    card2.append(card[l+d])
    suffle = []
    if len(card)%2 == 0:
        for q in range(d):
            suffle.append(card1[q])
            suffle.append(card2[q])
    else:
        if len(card)%2 == 1:
            for w in range(d):
                suffle.append(card1[w])
                suffle.append(card2[w])
            else:
                suffle.append(card1[d])
    print(f'#{t}', *suffle)