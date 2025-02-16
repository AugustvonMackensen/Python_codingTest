N, M = map(int, input().split())
first_matrix = []
second_matrix = []
# first matrix
for i in range(N):
    first_matrix.append(list(map(int, input().split())))
    if len(first_matrix[i]) > M:
        raise Exception('크기가 맞지 않습니다.')

# second matrix
for j in range(N):
    second_matrix.append(list(map(int, input().split())))
    if len(second_matrix[j]) > M:
        raise Exception('크기가 맞지 않습니다.')

for i in range(N):
    for j in range(M):
        print(first_matrix[i][j] + second_matrix[i][j], end=' ')
    print()


