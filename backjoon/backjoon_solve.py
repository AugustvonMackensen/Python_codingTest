'''
첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

출력
첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한
'''

num1 = int(input())
num2 = int(input())

# 곱하기 연산
third = num1 * int(str(num2)[2])
fourth = num1 * int(str(num2)[1])
fifth = num1 * int(str(num2)[0])
total = third + int(str(fourth) + '0') + int(str(fifth) + '00')
print(third)
print(fourth)
print(fifth)
print(total)