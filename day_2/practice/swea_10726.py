# 2d_practice
# 이진수 표현 (D3)
def main():
    T = int(input())

    def dec_to_bin(n):
        bin_ = ''
        while n:
            n, m = divmod(n, 2)
            bin_ += str(m)
        return bin_[::-1]

    for tc in range(1, T+1):
        N, M = map(int, input().split())
        bin_N = dec_to_bin(M)
        if sum(map(int, list(bin_N[-N:]))) == N:
            print(f"#{tc} ON")
        else: print(f"#{tc} OFF")


if __name__ == "__main__":
    main()