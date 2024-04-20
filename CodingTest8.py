'''
1부터 n까지의 모든 소수의 개수 구하기(에라스토테네스의 체)
'''

def solution(n):
    # 1부터 입력받은 숫자 n 사이에 있는 소수의 개수 반환 함수 구현
    # 소수 : 1과 자기 자신으로 나누어지는 수를 의미 함
    # 하나라도 약수가 되면 break -> 시간초과됨
    # 1 ~ 반으로 나눈걸로 소수 판정하기
    # 원리 2 : (효율성 25 + 정확성 75)
    # 원리 3 :

    i = 2
    prime_list = []

    while i <= n:
        if isPrime(i):
            prime_list.append(i)

        i += 1
    answer = len(prime_list)

    return answer


def isPrime(n):
    # 원시적 방법론 : O(N)
    # 원리 : n을 2로 나눠서, 2로 나눈 값보다 큰 정수로 수를 나누면 1<R<2인 실수 R이 나온다 -> 개수 구할때는 시간 초과됨 : O(N/2)
    # 원리2 : 제곱근 방법론 -> 제곱근
    flag = True
    for i in range(2, int(n  ** 0.5) + 1):
        if n % i == 0:
            flag = False
            break
    return flag


if __name__ == '__main__':
    print(solution(10))