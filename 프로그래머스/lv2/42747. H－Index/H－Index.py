def solution(citations):
    citations.sort()
    for idx , i in enumerate(citations):
        if i >= len(citations) - idx :
            return len(citations) - idx
    return 0