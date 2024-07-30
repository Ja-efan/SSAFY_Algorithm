# 햄버거 다이어트
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

import sys

sys.stdin = open("../inputs/input_5215.txt")


def is_available(ingredient, calorie):
    ig_cal = ingredient[1] + calorie
    if ig_cal > L:
        return False
    return True


def hamburger_diet(index, calorie, score):
    global max_score
    if index == N:
        max_score = max(max_score, score)
        return
    if calorie > L:
        return

    if is_available(ingredients[index], calorie):
        hamburger_diet(index+1, calorie+ingredients[index][1], score+ingredients[index][0])

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
