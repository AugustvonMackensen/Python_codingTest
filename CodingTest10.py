'''
Caesar Cipher Problem
'''
def solution(s, n):
    # ord : 문자 -> 아스키코드
    # chr : 아스키코드 -> 문자
    answer = ''
    for letter in s:
        if letter == ' ':
            answer += ' '
        elif letter.islower():
            answer += chr((ord(letter) - ord('a') + n) % 26 + ord('a'))
        elif letter.isupper():
            answer += chr((ord(letter) - ord('A') + n) % 26 + ord('A'))

        return answer
    # encoded_list = []
    # for i in range(len(s)):
    #     if s[i] != ' ': # 공백이 아니라면,
    #         character_idx = ord(s[i])
    #         encoded_idx = character_idx + n
    #         if (encoded_idx > 90 and encoded_idx < 97) or (encoded_idx > 122):
    #             encoded_idx = encoded_idx - 26
    #         encoded_list.append(chr(encoded_idx))
    #     else: # 공백인 경우
    #         encoded_list.append(s[i])
    # answer = ''.join(encoded_list) # 토큰 list -> 문자열로 만들기
    # return answer

if __name__ == '__main__':
    print(solution('a A z', 25)) # A-Z : 65 ~90, a-z :97~122