def solution(s):
    s = s.lower()
    answer = s.split(' ')
    for i in range(len(answer)):
        answer[i] = answer[i].capitalize()
    return ' '.join(answer)