# 농작물 수확하기 - D3

import sys

sys.stdin = open("../inputs/input_2805.txt")

T = int(input())  # 테스트 케이스의 개수
for tc in range(1, T + 1):
    N = int(input())  # 농장의 크기

    farm = [list(map(int, input().rstrip())) for _ in range(N)]  # 농장 초기화

    income = 0  # 농작물 수확 수익

    center_row = N // 2  # 농장의 가운데 열 (농장의 크기는 항상 홀수로 주어짐)
    income += sum(farm[center_row])  # 농장 가운데 열의 수익 추가

    for d in range(1, center_row + 1):  # 농장 가운데 열 기준으로 위/아래 행 수확
        # 가운데 열 기준 윗 방향
        upper_row = center_row - d
        # col = [d:-d]  # 가운데 열 기준으로 d칸 위 혹은 아래 열은 양 끝으로 d칸의 공백이 존재
        income += sum(farm[upper_row][d:-d])

        # 가운데 열 기준 아래 방향
        lower_row = center_row + d
        income += sum(farm[lower_row][d:-d])

    # 테스트 케이스 별 결과 출력
    print(f"#{tc} {income}")