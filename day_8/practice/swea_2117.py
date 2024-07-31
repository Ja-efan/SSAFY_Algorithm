# [모의 SW 역량테스트] 홈 방범 서비스
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

#  파일 입출력
import sys

sys.stdin = open("../inputs/input_2117.txt")


def cal_operation_cost(k):
    """
    cal_cost() 함수는 서비스 영역의 크기(k)에 따른 운영 비용을 계산하는 함수이다.
    :param k: 서비스 영역의 크기
    :return: 운영 비용
    """
    return k * k + (k - 1) * (k - 1)


def house_count(r, c, k):
    """
    house_count() 함수는 ...
    :param r:
    :param c:
    :param k:
    :return:
    """
    cnt = 0
    for i in range(k):
        if i == 0:
            """
            (r,c) 기준으로 
            """
            pass
        else:
            pass 
    return cnt


def cal_income_cost(r, c, k, m):
    """
    cal_income_cost() 함수는 (r,c)를 중심으로 하고,
    서비스 영역의 크기가 k인 영역에 대한 수익을 게산하는 함수이다.
    :param r:
    :param c:
    :param k:
    :param m:
    :return:
    """
    house_count = house_count(r, c, k)
    total_income = house_cnt * m
    return total_income


def service_area(r, c, k):
    """
    service_area() 함수는 좌표(r,c)를 기준으로 서비스 영억 k의 좌표 정보를 계산하는 함수이다.
    :param r: 행 좌표
    :param c: 열 좌표
    :param k: 서비스 영역의 크기
    :return: (r,c) 기준 서비스 영역의 상대 좌표 리스트
    """
    pass


T = int(input())  # 테스트 케이스 개수
for tc in range(1, T + 1):
    # N: 도시의 크기, M: 하나의 집이 지불할 수 있는 비용
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    house_cnt = sum(sum(city, []))  # 도시 내 집 개수
    MAX_M = M * house_cnt  # 최대 수익 (모든 집이 서비스 받는 경우)
    MAX_K = 1  # 서비스 영역의 최대 크기
    while cal_operation_cost(MAX_K + 1) <= MAX_M:
        MAX_K += 1

    for i in range(N):
        for j in range(N):
            k = 1
            while k < MAX_K:
                operation_cost = service_area(i, j, k)

                k += 1
