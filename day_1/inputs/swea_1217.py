# [S/W 문제해결 기본] 4일차 - 거듭 제곱
# D3

# recursion

import sys

sys.stdin = open("../inputs/input_1217.txt")

T = 10
for i in range(T):
    tc = int(input())  # 테스트 케이스 번호
    N, M = map(int, input().split())


    def exponential(n, m, res):
        if m == 0:
            return res
        else:
            return exponential(n, m - 1, res * n)


    result = exponential(N, M, 1)

    print(f"#{tc} {result}")
