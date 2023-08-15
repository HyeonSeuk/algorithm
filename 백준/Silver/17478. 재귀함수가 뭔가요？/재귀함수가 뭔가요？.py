cnt = 0  # 전역 변수

def chatbot(n):
    bar = '____'  # 들여쓰기를 위한 문자열
    global cnt  # 전역 변수 사용

    if n != cnt:
        print((bar*cnt)+'"재귀함수가 뭔가요?"')
        print((bar*cnt)+'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print((bar*cnt)+'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print((bar*cnt)+'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        cnt += 1  # 재귀 깊이 증가
        chatbot(n)  # 재귀 호출
    else:
        print((bar*cnt)+'"재귀함수가 뭔가요?"')  # 최대 깊이에 도달했을 때의 문장 출력
        print((bar*cnt)+'"재귀함수는 자기 자신을 호출하는 함수라네"')
        while True: # 재귀 깊이를 줄이면서 "라고 답변하였지." 문장 출력
            print((bar*cnt)+"라고 답변하였지.")
            cnt -= 1  # 재귀 깊이 감소
            if cnt < 0:  # 모든 재귀 깊이를 처리하면 루프 종료
                break
            
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')  # 시작 문장 출력
chatbot(int(input()))