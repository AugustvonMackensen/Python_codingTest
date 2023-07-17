import CodingTest1 as codt1
import CodingTest2 as codt2
import CodingTest3 as codt3

def soojebi(num):
    if num < 2:
        print(num, end='')
    else:
        soojebi(num // 2)
        print(num % 2, end='')


if __name__ == '__main__':
    print(codt1.solution(3, 12))
    print(codt1.solution(4, 6))
    print(codt2.solution(10))
    print(soojebi(20))