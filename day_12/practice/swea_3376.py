# 12d_practice
# 파도반 수열
# D3

def main():
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        memo = [0 for _ in range(101)]
        for i in range(1, 4):
            memo[i] = 1

        for i in range(3, N+1):
            memo[i] = memo[i-2] + memo[i-3]

        print(f"#{tc} {memo[N]}")


if __name__ == "__main__":
    import sys
    sys.stdin = open('../inputs/input_3376.txt')
    
    main()