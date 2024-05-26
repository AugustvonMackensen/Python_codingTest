def solution(n):
    # 문자열 -> 리스트의 reverse=True 옵션 사용
    num_list = list(str(n)) # list -> str
    num_list.sort(reverse=True)
    answer = int(''.join(num_list)) # ''.join을 이용하여 역순 정렬
    return answer

if __name__ == '__main__':
    print(solution(118372))