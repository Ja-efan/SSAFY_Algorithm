# 초심자의 회문 검사 - D3

import sys

sys.stdin = open("../inputs/input_1989.txt")

T = int(input())  # 테스트 케이스의 개수

for tc in range(1, T + 1):
    word = input()  # 사용자 입력 단어
    rev_word = word[::-1]  # 단어(문자열) 역순 배열(뒤집기)

    if word == rev_word:  # 입력 단어가 회문(Palindrome)인 경우
        print(f"#{tc} 1")  # 1 출력
    else:  # 회문이 아닌 경우
        print(f"#{tc} 0")  # 2 출력
