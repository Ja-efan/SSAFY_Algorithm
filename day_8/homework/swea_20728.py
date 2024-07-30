# 공평한 분배 2
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

import sys

sys.stdin = open("../inputs/input_20728.txt")

T = int(input())

for tc in range(1, T + 1):
    # N: 전체 주머니의 개수
    # K: 나눠줄 주머니의 개수
    N, K = map(int, input().split())

    # 주머니 속 사탕의 개수 리스트
    candies = list(map(int, input().split()))

    # candies 내림차순 정렬
    candies.sort(reverse=True)

    # 무한 상수 선언
    INF = float("inf")

    # 최소 차이 초기값
    min_diff = INF

    # 정렬된 candies 에서 모든 가능한 K개 선택에 대하여
    for i in range(N-K+1):
        # 최대 사탕 개수
        max_candies = candies[i:i+K][0]

        # 최소 사탕 개수
        min_candies = candies[i:i+K][-1]

        # 최대 최소 차이
        diff = max_candies - min_candies

        # 최소 차이 갱신
        min_diff = min(min_diff, diff)

    print(f"#{tc} {min_diff}")
