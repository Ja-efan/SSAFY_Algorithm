# 부분 수열의 합
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

import sys

sys.stdin = open("../inputs/input_2817.txt")


# count를 관리할 클래스
# 240730 IDEA
class Counter:
    def __init__(self):
        self.count = 0

    def add_count(self):
        self.count += 1


def make_target(arr, index, target, acc, counter):
    if acc == target:
        # 누적 합이 k와 동일해진 경우
        counter.add_count()  # count 하나 올리고
        return  # 리턴

    if index == len(arr):  # 주어진 배열을 모두 순회한 경우
        return  # 리턴

    if acc + arr[index] > target:
        # 주어진 배열이 오름차순으로 정렬되어있기 때문에 현재 숫자를 더해서 target이상이 된다면,
        # 다음 숫자를 더해도 target 보다 커지게 된다.
        return

    # 현재 숫자 포함
    make_target(arr=arr, index=index + 1, target=target, acc=acc + arr[index], counter=counter)

    # 현재 숫자 미포함
    make_target(arr=arr, index=index + 1, target=target, acc=acc, counter=counter)


T = int(input())  # 테스트 케이스 개수
for tc in range(1, T + 1):
    N, K = map(int, input().rstrip().split())  # N: 자연수 개수, K: 타겟 넘버

    numbers = list(map(int, input().rstrip().split()))

    numbers.sort()  # 오름차순으로 정렬
    idx = 0
    summ = 0
    cnt = Counter()
    make_target(arr=numbers, index=idx, target=K, acc=summ, counter=cnt)
    print(f"#{tc} {cnt.count}")
