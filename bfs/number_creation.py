# import sys
# sys.stdin = open("input_4008.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    op_list = list(map(int, input().split()))
    number_list = list(map(int, input().split()))
    # 문제에서 원하는 수식 결과의 최댓값과 최솟값을 구해야 한다.

    # 문제에서 주어진 조건
    min_num = 100000000
    max_num = -100000000


    def create_num(op_list, idx, res):
        """
        :param op_list: 남은 연산자 (사실상 visited 역할을 한다. 대신 T/F 가 아닌 숫자로 취급, 0이 되면 False와 동일)
        :param idx: 이번에 선택한 숫자
        :param res: 지금까지 누적된 결과
        :return: None
        """
        global max_num, min_num

        if idx == N:  # 모든 숫자를 다 계산했다면 결과 반영
            max_num = max(max_num, res)
            min_num = min(min_num, res)
            return

        for op_idx, op_cnt in enumerate(op_list):
            if op_cnt == 0:
                continue
            tmp_res = res
            if op_idx == 0:  # +
                tmp_res += number_list[idx]
            elif op_idx == 1:  # -
                tmp_res -= number_list[idx]
            elif op_idx == 2:  # *
                tmp_res *= number_list[idx]
            elif op_idx ==3:  # /
                tmp_res = int(tmp_res / number_list[idx])

            op_list[op_idx] -= 1
            create_num(op_list, idx+1, tmp_res)
            op_list[op_idx] += 1


    # DFS 구현에 있어 중요한 것
    # 1. 재귀호출을 중단할 파라미터 (어떤 숫자를 선택하고 있는지, 인덱스)
    # 2. 누적해서 가져갈 결과 파라미터 (지금까지 수식에서 나온 결과를 전달)
    # 3. 연산자 목록 -> visited

    init_num = number_list[0]
    init_idx = 1
    # 주어진 숫자의 순서를 변경할 수 없음
    # 문제에서 숫자 한 개는 고르고 들어감
    create_num(op_list, init_idx, init_num)
    print(f"#{tc} {max_num - min_num}")