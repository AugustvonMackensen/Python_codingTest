
'''
k 번째 수
'''
def solution(array, commands):
    # 1. command 인자의 [first, last, pos]에서 array를 [first:last]로 쪼개고, pos의 숫자를 배열에 담아 리턴
    # 2. command 수만큼 반복
    answer = []
    num_array = []
    for command in commands:
        num_array = array[(command[0]-1):command[1]]
        num_array.sort()
        answer.append(num_array[(command[2]-1)])
    return answer

if __name__ == '__main__':
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))