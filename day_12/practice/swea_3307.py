# 12d_practice
# 최장 증가 부분 수열
# D3

def main():
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        elements = [0] + list(map(int, input().split()))
        memo = [0 for _ in range(N+1)]
        memo[1] = 1

        for i in range(2, N+1):
            for j in range(i):
                if elements[i] > elements[j]:
                    memo[i] = max(memo[i], memo[j] + 1)

        print(f"#{tc} {max(memo)}")


if __name__ == "__main__":
    import sys
    sys.stdin = open("../inputs/input_3307.txt")
    main()