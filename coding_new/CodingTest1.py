

def solution(num_list):
    # next 함수 사용
    # next 함수 안에 for문과 if 조건절을 넣어 음수인 수를 찾아내는 인덱스를 구함.
    # 음수가 없으면 -1 리턴
    try:
        answer = num_list.index(next(i for i in num_list if i < 0))
    except StopIteration:
        answer = -1

    return answer

if __name__ == '__main__':
    print(solution([12, 4, 15, 46, 38, -2, 15]))