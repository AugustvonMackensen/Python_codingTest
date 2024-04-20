def solution(arr):
    answer = []
    length = len(arr)

    if length > 1:
        answer = arr.copy()
        answer.remove(min(answer))
    else:
        answer.append(-1)

    return answer

if __name__ == '__main__':
    print(solution([4,3,2,1]))
    print(solution([10]))