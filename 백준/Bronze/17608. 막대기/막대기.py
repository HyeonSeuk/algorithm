import sys
input = sys.stdin.readline

stack = [] # 빈 스택 생성
cnt = 0 # 개수를 셀 카운트
number = 0 # 비교를 위한 변수
a = int(input()) # 반복 개수 선언을 위한 변수 생성
for i in range(a):
    stack.append(int(input())) # 빈 스택에 넣어준다

for j in reversed(stack): # 오른쪽을 기준으로 계산해야 하므로 뒤집는다
    if number < j: # 값이 크다면 오른쪽에서 보인다는 뜻
        number = j 
        cnt += 1  # 보이는 개수를 카운트
print(cnt)