# 타일 붙이기
# DP


def main():
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        memo = [0 for _ in range(N+1)]

        memo[1] = 1
        memo[2] = 3
        memo[3] = 6

        """
        2xN 직사각형은 2x(N-i)보다 i 만큼 공간이 더 크므로,
        2x(N-i) 공간을 채우는 경우의 수에 2xi 공간을 채우는 경우의 수를 곱해준다. (1<= i <= 3)
        이때, i가 2인 경우는 i가 1인 경우에 의해서 결정적으로 정해지는 케이스가 있으므로, 해당 케이스를 제외해주어야 한다.
        동일하게, i가 3인 경우도 i가 1인 경우와 2인 경우에 의해 결정적으로 정해지는 케이스를 제외시켜준다.
         
        점화식 :
        f(n) = (f(n-1) * f(1))
                + (f(n-2) * (f(2) - f(1))) 
                    + (f(n-3) * (f(3) - f(2) - f(1) - f(1)))
        """
        for i in range(4, N+1):
            memo[i] = memo[i-1] * memo[1] + \
                      memo[i-2] * (memo[2] - memo[1]) + \
                      memo[i-3] * (memo[3] - memo[2] - (2*memo[1]))  # memo[i-3] * 1

        print(memo)
        print(f"#{tc} {memo[-1]}")


if __name__ == "__main__":
    main()