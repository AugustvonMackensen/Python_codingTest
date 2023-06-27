import math

# Find the GCD and LCM for two numbers
# 두 수의 최대공약수와 최소공배수 구하기


def solution(n, m):
    answer = []

    for i in range(min(n, m), 0, -1):  # 1씩 감소시킴
        if n % i == 0 and m % i == 0:
            gcd = i
            a = n // i
            b = m // i
            lcm = i * a * b
            answer.append(gcd)
            answer.append(lcm)
            break
    return answer





