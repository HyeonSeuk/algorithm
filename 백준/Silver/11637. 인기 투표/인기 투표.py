T = int(input())

for i in range(T):
    n = int(input())
    votes = []
    total_votes = 0
    
    for j in range(n):
        v = int(input())
        votes.append(v)
        total_votes += v
    
    max_vote = max(votes)  
    max_idx = votes.index(max_vote) + 1  
    
    if votes.count(max_vote) == 1 and max_vote > total_votes / 2:
        print("majority winner", max_idx)
    
    elif votes.count(max_vote) == 1 and max_vote <= total_votes / 2:
        print("minority winner", max_idx)

    else:
        print("no winner")