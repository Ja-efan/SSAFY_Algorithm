# 2d_practice
# 쇠막대기 자르기 (D4)

def main():
    T = int(input())
    for tc in range(1, T+1):
        inputs = input()
        rev_inputs = list(inputs[::-1])
        stack = []
        cut_cnt = 0
        while rev_inputs:
            item = rev_inputs.pop()
            if item == "(":
                if rev_inputs[-1] == ")":  # 레이저
                    rev_inputs.pop()  # 레이저 마저 제거 해주고,
                    if not stack:  # 자를 막대기가 없다면 스킵
                        continue
                    cut_cnt += len(stack)  # 막대기 개수 만큼 커팅
                else:  # 막대기 인 경우 -> stack 추가
                    stack.append(item)
            elif item == ")":  # 막대기 끝 부분인 경우 (위에서 레이저인 경우를 모두 제거 해주었음)
                stack.pop()  # 막대기 하나 제거
                cut_cnt += 1  # 남은 막대기 부분 커팅 추가

        print(cut_cnt)


if __name__ == "__main__":
    main()