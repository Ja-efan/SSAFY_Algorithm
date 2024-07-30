# 진용이네 주차타워
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AW9j74FacD0DFAUY

import sys
from collections import deque
import heapq

sys.stdin = open("./inputs/input_9280.txt")



T  = int(input())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    n, m = map(int, input())  # n: 주차 공간 개수, m: 주차 할 차량 수
    cost = [int(input()) for _ in range(n)]
    weights = [int(input()) for _ in range(m)]






