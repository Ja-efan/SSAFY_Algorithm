from itertools import combinations

# import sys
# sys.stdin = open("../inputs/input_2115.txt")

T = int(input())  # 테스트 케이스 개수

for tc in range(1, T+1):
    #  N: 벌통들의 크기 , M: 선택할 수 있는 벌통의 개수, C: 채취할 수 있는 꿀의 최대 양
    N, M, C = map(int, input().split())

    # 벌통
    honey_grid = [list(map(int, input().split())) for _ in range(N)]

    """
    두 명의 일꾼이 있으며, 각각의 일꾼은 가로로 연속되게 M개의 벌통을 선택하고,
    선택한 벌통에서 꿀을 채취할 수 있다.
    단, 두 명의 일꾼이 선택한 벌통은 서로 겹치면 안 된다.
    """
    """
    한 일꾼이 작업을 하는 벌통을 제외한 곳 중 M개의 벌통이 연속적으로 있는 경우를 모두 계산?
    """
    def cal_max_profit(honey_row):
        subset = []
        for i in range(1, M+1):
            combs = combinations(honey_row, i)
            subset.extend(list(combs))

        max_profit = 0
        for comb in subset:
            sum_comb = sum(list(comb))
            if sum_comb > C:
                continue
            else:
                tmp_profit = 0
                for honey in comb:
                    tmp_profit += (honey**2)
                max_profit = max(max_profit, tmp_profit)
        return max_profit

    total_profit = 0  # 총 수익

    # 일꾼 1이 전체적으로 순회
    for i in range(N):
        for j in range(N-M+1):
            honey_pot_1 = honey_grid[i][j:j+M]
            worker1_max_profit = cal_max_profit(honey_pot_1)
            for k in range(N):
                for l in range(N-M+1):
                    if k == i and ((j <= l <= j+M-1) or (j<= l+M <= j+M-1)):
                        continue
                    honey_pot_2 = honey_grid[k][l:l+M]
                    worker2_max_profit = cal_max_profit(honey_pot_2)

                    tmp_total_profit = worker1_max_profit + worker2_max_profit
                    total_profit = max(total_profit, tmp_total_profit)

    print(f"#{tc} {total_profit}")



