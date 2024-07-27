# [모의 SW 역량테스트] 숫자 만들기

# 연산자의 우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산
# 주어진 연산자 카드를 사용하여 수식을 계산했을 때,
# 그 결과가 최대가 되는 수식과 최소가 되는 수쉭을 찾고,
# 두 값의 차이를 출력

"""
1. 숫자를 고르고
2. 연산자를 고르고
3. 다음 숫자를 골라라


"""
def solution():
    T = int(input())  # 총 테스트 케이스 개수
    for tc in range(1, T+1):
        N = int(input())  # 숫자의 개수
        num_operators = list(map(int, input().split()))  # 연산자 개수
        nums = list(map(int, input().split()))


