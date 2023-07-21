def solution(numer1, denom1, numer2, denom2):

    # if both of denoms are same
    if denom1 == denom2:
        addition_denom = denom1
        addition_numer = numer1 + numer2  # then just add 2 numers
    else:
        # if both denoms are Prime number
        if isPrime(denom1) or isPrime(denom2):
            addition_denom = denom1 * denom2
            addition_numer = numer1 * denom2 + numer2 * denom1
        else:
            addition_denom = getLcm(denom1, denom2)
            addition_numer = numer1 * (addition_denom // denom1) \
                             + numer2 * (addition_denom //denom2)


    if addition_numer % addition_denom == 0:
        addition_numer = addition_numer // addition_denom
        addition_denom = addition_denom // addition_denom
    elif getGcd(addition_numer, addition_denom) > 1:
        gcd = getGcd(addition_numer, addition_denom)
        addition_numer = addition_numer // gcd
        addition_denom = addition_denom // gcd


    answer = [addition_numer, addition_denom]  # fraction answer
    return answer


def isPrime(num):
    # Returns True if it is a prime Number
    for i in range(2, num):
        if (num % i == 0):
            return False

    return True

def getGcd(num1, num2):
    gcd = 1
    if not (isPrime(num1) and isPrime(num2)):
        # Python은  if else로 삼항연산자 처리. C/C++/java는 조건식? true : false 값 이런식으로 처리함
        number = num1 if num1 < num2 else num2
        for i in range(2, number + 1):
            if num1 % i == 0 and num2 % i == 0:
                gcd = i
    return gcd


def getLcm(num1, num2):
    gcd = getGcd(num1, num2)
    mul1 = num1 // gcd
    mul2 = num2 // gcd
    return gcd * mul1 * mul2


if __name__ == '__main__':
    print(solution(1, 2, 3, 4))
    print(solution(9, 2, 1, 3))
    print(solution(4, 4, 4, 4))
    print(solution(1, 4, 2, 6))