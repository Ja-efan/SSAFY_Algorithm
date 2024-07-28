# [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드
# D3

import sys

sys.stdin = open("../inputs/input_1240.txt")

# 암호코드의 숫자가 암호화되는 규칙
# 모든 코드가 0으로 시작해서 1로 끝난다.
enc_rules = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9
}

T = int(input())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 배열의 세로 크기 N, 가로 크기 M
    arr = []  # 사용자 입력 저장 배열
    code_start_idx = 0  # 암호 시작 인덱스
    code_end_idx = 0  # 암호 끝 인덱스
    bits_code = []  # 비트로 구성된 암호 코드 리스트
    for i in range(N):
        row = input().rstrip()
        if bits_code:  # 이미 코드를 찾은 경우 아래 코드 스킵
            continue
        row_list = list(map(int, list(row)))

        is_code = sum(row_list)  # 해당 열을 모두 더함 으로써 코드 인지 확인 (합이 0이면 코드 x, 합이 1이상 이면 코드 o)
        if is_code:
            rev_row = row[::-1]
            for j in range(len(rev_row)):
                if int(rev_row[j]) == 1:  # 모든 코드의 끝 부분이 1로 끝나는 규칙을 이용
                    code_start_idx = j  # rev_row 에서 암호 코드가 시작 하는 인덱스
                    code_end_idx = j + 56  # rev_row 에서 암호 코드가 끝나는 인덱스
                    break
            # rev_row 에서 start_idx 와 end_idx 를 지정 했기 때문에 실제 암호 코드는 역순으로 지정
            rev_code = rev_row[code_start_idx: code_end_idx]
            bits_code = rev_code[::-1]

    enc_code = []  # 숫자로 구성된 암호 코드
    for i in range(0, len(bits_code), 7):
        # 하나의 숫자는 7개의 비트로 이루어져 있으므로, step은 7로 할당
        bits = bits_code[i:i+7]  # 7비트씩 끊어줌
        bits2int = enc_rules[bits]  # 암호화 규칙에서 비트를 숫자로 변환
        enc_code.append(bits2int)  # 변환된 숫자를 암호 코드에 추가

    even_sum = 0  # 짝수 자리의 합
    odd_sum = 0  # 홀수 자리의 합
    for i in range(len(enc_code)):
        if i % 2 == 0:  # idx가 짝수인 경우
            even_sum += enc_code[i]
        else:  # idx가 홀수인 경우
            odd_sum += enc_code[i]

    # 해당 암호 코드가 유효한 코드인지 확인
    # (홀수 자리의 합) x 3 + (짝수 자리의 합)이 10의 배수인 경우 유효 하므로,
    # 아래 식이 0인 경우 유효 하다.
    # 1 이상의 값을 갖는 경우 조건문에서 True로 인식하기 때문에 변수명은 not_valid로 작성
    is_not_valid_code = (even_sum * 3 + odd_sum) % 10

    if is_not_valid_code:  # 해당 코드가 유효하지 않은 경우
        print(f"#{tc} {0}")
    else:  # 해당 코드가 유효한 경우
        print(f"#{tc} {odd_sum + even_sum}")

