# 15d_homework
# 특별한 정렬 (D3)

from collections import deque


def main():
    T = int(input())

    for tc in range(1, T+1):
        N = int(input())
        numbers = list(map(int, input().split()))

        numbers.sort()
        numbers = deque(numbers)
        result = []

        for i in range(10):
            if i % 2 == 0:
                # 현 시점 가장 큰 수 추가
                result.append(str(numbers.pop()))
            else:
                # 가장 작은 수 추가
                result.append(str(numbers.popleft()))

        result = " ".join(result)

        print(f"#{tc} {result}")


if __name__ == "__main__":
    import sys
    sys.stdin = open("../inputs/input_19646.txt")
    main()