Y = []           # 빈 리스트 2개를 생성
K = []
for i in range(10):     # Y대학 점수까지만 Y리스트에 더한다
    Y.append(int(input()))
for j in range(10):     # 나머지 K대학 점수를 K리스트에 더한다
    K.append(int(input()))
Y.sort()       # 값을 작은 ~ 큰 숫자 순으로 정렬
K.sort()
print(sum(Y[7:]), sum(K[7:]))  # 큰 수 3개를 더하여 결과 출력