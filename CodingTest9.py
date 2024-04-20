'''
1부터 n까지의 모든 소수의 개수 구하기(에라스토테네스의 체)
'''

def solution(n):
    # 1부터 입력받은 숫자 n 사이에 있는 소수의 개수 반환 함수 구현
    # 소수 : 1과 자기 자신으로 나누어지는 수를 의미 함
    # 하나라도 약수가 되면 break -> 시간초과됨
    # 에라스토테네스의 체 사용

    prime_set = set(range(2, n + 1))  # 2~n까지 숫자 set자료형으로 선언 및 할당
    for i in range(2, n + 1):
        if i in prime_set:
            prime_set -= set(range(i * 2, n + 1, i))# 어떤 수 자신을 제외한 어떤 수의 배수 제거
    return len(prime_set)

if __name__ == '__main__':
    print(solution(10))