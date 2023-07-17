def solution(n):
    # Count the Prime Numbers
    answer = 0

    for i in range(1, n):  # 1~ n
        for j in range(1, i):
            if i % j != 0:
                answer += 1  # 파이썬은 가독성 측면에서 증감 연산자 선호하지 않음

    return answer
