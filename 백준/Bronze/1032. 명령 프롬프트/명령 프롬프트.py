n = int(input())
a = list(input()) # 첫번째 단어
leg = len(a) # 첫번째 단어 길이
for i in range(n-1): # 이미 단어를 받았으니 나머지 단어와 비교를 위해 n-1
    b = list(input()) # 비교할 단어
    for j in range(leg): # 단어의 길이는 모두 같으니 첫번째 단어의 길이 기준으로 반복
        if a[j] != b[j]: # 단어를 1개씩 비교
            a[j] = '?' # 단어가 같지않은 부분은 ?로 변경
print(''.join(a))