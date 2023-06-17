def solution(numbers):
    lst = []
    for i in range(1, 10):
        if i not in numbers:
            lst.append(i)
    answer = sum(lst)
    return answer