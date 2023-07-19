# time cost problem

def solution(s):
    answer = 0
    s = s.split()
    for i in range(len(s)):

        if(s[i] == 'Z'):
            answer -= int(s[i - 1])  # if s[i] is 'Z', then subtract last number from the answer.
        else:
            answer += int(s[i])  # add it to the answer

    return answer

if __name__ == '__main__':
    print(solution('1 2 Z 3'))
    print(solution('-1 -2 -3 Z'))