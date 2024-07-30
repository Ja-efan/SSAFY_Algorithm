# 햄버거 다이어트
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

import sys

sys.stdin = open("../inputs/input_5215.txt")


def is_available(ingredient, calorie):
    """
    해당 재료를 추가할 수 있는지 검사하는 함수
    :param ingredient: 재료 정보 (재료 점수, 재료 칼로리)
    :param calorie: 누적 칼로리
    :return: 해당 재료 추가 가능 여부
    """
    ig_cal = ingredient[1] + calorie
    if ig_cal > L:  # 주어진 제한 칼로리를 넘어가는 경우
        return False  # 추가 불가능
    return True  # 추가 가능


def hamburger_diet(index, calorie, score):
    """
    햄버거를 만드는 함수
    :param index: 재료 인덱스(번호)
    :param calorie: 누적 칼로리
    :param score: 누적 점수
    :return: None
    """
    global max_score  # 전역 변수 max_score 관리
    if index == N:  # 마지막 재료까지 더한 경우
        max_score = max(max_score, score)  # max_score 갱신
        return
    if calorie > L:  # 누적 칼로리가 제한 칼로리보다 높은 경우
        return

    if is_available(ingredients[index], calorie):
        # 현재 재료가 추가될 수 있는 경우
        # 다음 재료에 대한 recursion
        # 칼로리와 점수 갱신
        hamburger_diet(index+1, calorie+ingredients[index][1], score+ingredients[index][0])

    # 현재 재료 추가가 불가한 경우
    # 다음 재료에 대한 recursion
    hamburger_diet(index + 1, calorie, score)

T = int(input())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    N, L = map(int, input().rstrip().split())  # N: 재료의 수, L: 제한 칼로리

    # 재료 리스트 : [(점수, 칼로리), ..]
    ingredients = [tuple(map(int, input().rstrip().split())) for _ in range(N)]

    max_score = 0
    calorie = 0
    hamburger_diet(0, calorie, max_score)
    print(f"#{tc} {max_score}")
