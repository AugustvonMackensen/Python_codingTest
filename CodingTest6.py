# find the Integer part for the value(num1 / num2 * 1000)
# use Math module and use function floor() to get rid of float/double part
import math
def solution(num1, num2):
    val = num1 / num2 * 1000

    answer = math.floor(val)
    return answer

if __name__ == '__main__':
    print(solution(3, 2))
    print(solution(7, 3))
    print(solution(1, 16))