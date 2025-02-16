N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))

num_list = sorted(num_list)
for item in num_list:
    print(f'{item}')