from itertools import combinations

import sys
sys.stdin = open("../inputs/input_2115.txt")

T = int(input())  # 테스트 케이스 개수

for tc in range(1, T+1):
    #  N: 벌통들의 크기 , M: 선택할 수 있는 벌통의 개수, C: 채취할 수 있는 꿀의 최대 양
    N, M, C = map(int, input().split())

    # 벌통
    honey_grid = [list(map(int, input().split())) for _ in range(N)]

    def dfs(honey_index, honey_benefit, honey_sum, x, y):
        global part_sum

        # 가지치기
        # 이미 C를 넘었으면, 부분집합이 늘어나면 무조건 C를 넘음으로 중단
        if honey_sum > C :
            return
        # 가리키는 꿀의 인덱스가 M에 도달하며 ㄴ중ㄷ나
        if honey_index == M:
            part_sum = max(part_sum, honey_benefit)

        cnt_benefit =
        cnt_sum =
        # 부분집합을 구하는 것과 같이 진행
        # 현재 꿀을 선택하거나
        dfs(honey_index + 1, honey_benefit + cnt_benefit, honey_sum, x, y)
        # 현재 꿀을 선택하지 않거나
        dfs(honey_index + 1, honey_benefit, honey_sum, x, y)

    for fst_i in range(N):
        for fst_j in range(N-M+1):
            part_sum = 0  # 아래 DFS를 통해서 얻은 최대 이익을 저장할 변수
            # 부분집합의 최대 이익을 구하고,
            # 중간에 부분집합의 합이 C를 넘으면 가지치기가 가능
            # DFS 함수를 호출할 때 필요한 것
            # 1. 재귀를 중단할 파라미터  => 선택할 벌통 인덱스 (M 에 도달하면 중단)
            # 2. 누적해서 원하는 결과값  => 각 꿀의 제곱을 합한 꿀의 이익
            # 3. 시작 위치
            # 4. 가지치기를 위해서 (지금까지 합한 꿀의 양)

            # 선택할 벌통 인덱스, 꿀의 누적 이익, 꿀의 누적합, 현재 시작 좌표
            dfs(0, )
            fst_max = part_sum
