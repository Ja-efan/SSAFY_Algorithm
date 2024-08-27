# 10d_homework
# 그룹 나누기

import sys
from collections import deque

"""
풀이 설명 :
    BFS로 섬찾기 문제와 동일하게 접근 
"""


def bfs():
    T = int(input())  # 테스트 케이스 개수
    for tc in range(1, T + 1):
        N, M = map(int, input().split())  # N: 출석 번호, M: 신청서 개수

        numbers = list(map(int, input().split()))

        pairs = [(numbers[i], numbers[i + 1]) for i in range(0, 2 * M - 1, 2)]  # tuple list로 재구성

        pair_dict = {i: [] for i in range(1, N + 1)}  # 인접 리스트 딕셔너리
        for f, s in pairs:
            pair_dict[f].append(s)
            pair_dict[s].append(f)

        group_cnt = 0
        is_selected = set()  # 중복 방지 집합
        for i in range(1, N + 1):
            if i in is_selected: continue  # 이미 조에 편성된 경우
            is_selected.add(i)  # 조 편성 완료 처리
            dq = deque(pair_dict[i])  # deque 변환
            while dq:
                tmp = dq.popleft()
                if tmp not in is_selected:  # 조 편성이 안된 경우
                    is_selected.add(tmp)  # 조 편성 완료 처리
                    dq.extend(pair_dict[tmp])  # 인접한 정점 추가 (pair_dict의 value 타입이 list이기 때문에 extend)
            group_cnt += 1

        print(f"#{tc} {group_cnt}")


if __name__ == "__main__":
    sys.stdin = open("../inputs/input_5248.txt")
    bfs()
