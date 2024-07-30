# [모의 SW 역량테스트] 보물상자  비밀번호
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZC_w6Z6yygDFAQW&contestProbId=AWXRUN9KfZ8DFAUo&probBoxId=AZDJWmAq-hkDFAVs&type=PROBLEM&problemBoxTitle=2w_homework&problemBoxCnt=3
# import sys
#
# sys.stdin = open("../inputs/input_5658.txt")

# # hexadecimal dictionary
# hex_list = list("ABCDEF")
# hexadecimal_dict = dict()
# for a, hex in zip(hex_list, range(10, 10 + len(hex_list))):
#     hexadecimal_dict[a] = hex

T = int(input())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N: 숫자 개수(4의 배수), K: 크기 순서
    numbers = list(input().rstrip())  # 자물쇠에 존재하는 숫자 리스트

    line_numbers = N // 4  # 한 변에 존재하는 숫자 개수

    # 비밀번호 중복 방지를 위한 set 정의
    candidate_password_set = set()

    # 시계방향으로 회전하며 후보 비밀번호를 구성
    for rotate_n in range(line_numbers):  # 한 변에 존재하는 숫자 개수 만큼 회전 시 0회전과 동일
        # rotate_n: 회전 수 (0, 1, 2)
        # 시계방향 회전
        rotated_numbers = []  # 회전 된 숫자 리스트
        if not rotate_n:  # 0회전인 경우
            rotated_numbers = numbers[:]
        elif rotate_n:  # 1회전 이상인 경우
            rotated_numbers = numbers[-rotate_n:] + numbers[:-rotate_n]

        idx = 0  # numbers 슬라이싱 할 인덱스
        while idx < N:  # numbers 길이 벗어나지 않는 범위 내에서 후보 비밀번호 구성
            candidate_password = "".join(rotated_numbers[idx:idx + line_numbers])
            candidate_password_set.add(candidate_password)  # 후보 비밀번호 set 에 추가
            idx += line_numbers  # idx 갱신

    # 형 변환 (set -> list)
    candidate_password_list = []
    for hexadecimal_pw in candidate_password_set:
        decimal_pw = int(hexadecimal_pw, 16)  # string 으로 표현 된 16진수를 10진수로 변경
        candidate_password_list.append(decimal_pw)

    # 비밀번호 정렬 (내림차순)
    candidate_password_list.sort(reverse=True)

    # 비밀번호 출력 (K번째 큰 수)
    print(f"#{tc} {candidate_password_list[K-1]}")
