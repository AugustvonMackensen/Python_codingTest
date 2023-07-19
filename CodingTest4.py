def solution(n):
    # Big Rectangle : Width = n, Height : 3
    # small tile : width = 2, height = 1
    big_length = 2 * (3 + n)
    position_list = []

    # Entire Rectangle Board
    for i in range(big_length):
        position_list.append(i)

    for j in range(big_length):
        if(position_list[j] == j):
            position_list[j] = '*'
        else:
            continue


if __name__ == '__main__':
    print(solution(10))