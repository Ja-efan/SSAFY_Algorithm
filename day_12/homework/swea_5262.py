# 12d_homework
# 정렬된 부분 집합 (D4)
# LIS

def main():
    T = int(input())
    for tc in range(1, T+1):
        # 입력 전처리
        numbers = list(map(int, input().split()))
        N = numbers[0]
        numbers = numbers[1:]

        # memoization
        memo = [1 for _ in range(N)]
        # 모든 원소를 마지막으로 하는 sub-sequence 순회
        for i in range(N):
            for j in range(i+1):
                # i가 j보다 크면, j를 마지막으로 하는 sub-sequence에 i를 추가하면 됨
                if numbers[j] < numbers[i]:
                    memo[i] = max(memo[i], memo[j]+1)

        print(f"#{tc} {max(memo)}")



if __name__ == "__main__":
    main()