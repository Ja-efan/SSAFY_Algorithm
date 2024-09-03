# 14d_homework
# Contact
# D4
"""
비상연락망과 연락을 시작하는 당번에 대한 정보가 주어질 때,
가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람을 구하는 함수를 작성하시오.

"""
from collections import defaultdict


def main():
    T = 10
    for tc in range(1, T+1):
        N, SOURCE = map(int, input().split())
        from_to_list = list(map(int, input().split()))

        edges = [(from_to_list[i], from_to_list[i+1]) for i in range(0, N-1, 2)]
        contact = defaultdict(set)
        for edge in edges:
            s, e = edge
            contact[s].add(e)

        visited = {SOURCE}
        stack = [SOURCE]
        while stack:
            tmp_stack = []
            for i in range(len(stack)):
                for adj in contact[stack[i]]:
                    if adj not in visited:
                        tmp_stack.append(adj)
                        visited.add(adj)
            # stack에 있는 정점이 마지막 정점
            if not tmp_stack:
                print(f"#{tc} {max(stack)}")
                break
            stack = tmp_stack[:]


if __name__ == "__main__":
    import sys
    sys.stdin = open("../inputs/input_1238.txt")
    main()