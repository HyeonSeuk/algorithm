a, b = list(map(int, input().split())) # 숫자 2개를 받는다
numbers = list(map(int, input().split())) # 숫자들을 리스트로 넣는다

for i in numbers: # 반복문
    if b > i: # 만약 조건 대로 숫자가 리스트의 숫자들이 작다면
        print(i, end=' ') # 해당 순서대로 출력을 해라