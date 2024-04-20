def solution(n):
    square = n ** 0.5
    if square.is_integer():
        return int((square + 1) ** 2)
    else:
        return -1



if __name__ == '__main__':
    print(solution(144))
    print(solution(87))