# [모의 SW 역량테스트] 원자 소멸 시뮬레이션
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

import sys

sys.stdin = open("../inputs/input_5648.txt")

directions = {
    0: [0, 1],  # 상
    1: [0, -1],  # 하
    2: [-1, 0],  # 좌
    3: [1, 0]  # 우
}
"""
두 원자가 충돌하는 경우 
    두 원자가 직선상에서 만나는 경우 
        상 - 하 
        좌 - 우 
    두 원자가 수직으로 만나는 경우 
        상 - 우
        상 - 좌 
        하 - 우 
        하 - 좌 
세 원자가 충돌하는 경우 
    상 - 우 - 하 
    상 - 우 - 좌
"""

"""
원자들의 수 N은 1000개 이하이다.

원자들의 위치는 -1000 이상 1000이하의 정수로 주어진다.
원자들이 움직일 수 있는 좌표의 범위에 제한은 없다.

현재 원자를 기준으로 충돌 가능성이 있는 원자들을 후보 충돌 원자로 설정.
"""


def check_extinction(atom1, atom2):
    """
    :param atom1: 원자 1의 정보 (x, y ,d, k)
    :param atom2: 원자 2의 정보 (x, y, d, k)
    :return: boolean (두 원자가 충돌 가능성이 있는 경우 True, 충돌 가능성이 없다면 False)
    """
    atom1_x, atom1_y, atom1_d, _ = atom1
    atom2_x, atom2_y, atom2_d, _ = atom2

    # 두 원자가 평행하게 움직이는 경우 (서로 다른 열 -> 좌/우로 움직임)
    if atom1_y != atom2_y and atom1_d >= 2 and atom2_d >= 2:
        return False
        # 두 원자가 평행하게 움직이는 경우 2 (서로 다른 행 -> 위/아래로 움직임)
    if atom1_x != atom2_x and atom1_d <= 1 and atom2_d <= 1:
        return False
        # 두 원자가 같은 y좌표에서 에서 같은 방향으로 움직이는 경우
    if atom1_y == atom2_y and atom1_d == atom2_d:
        return False
    # 두 원자가 같은 x좌표에서 같은 방향으로 움직이는 경우
    if atom1_x == atom2_x and atom1_d == atom2_d:
        return False

    # 충돌 가능성이 있는 경우
    return True


def delete_element(lst:list, idx:int) -> list :
    lst[idx] = lst[-1]
    lst.pop()
    return lst


def atom_extinction(atoms):
    total_energy = 0
    while atoms:
        atom = atoms.pop()
        extinction_candidate = []  # 현재 원자와 충돌 가능성이 있는 후보 원자 리스트
        for i in range(len(atoms)):
            if atoms[i][0] == atom[0] and atoms[i][1] == atom[1]:
                continue
            atom2 = atoms[i]
            if check_extinction(atom1=atom, atom2=atom2):
                extinction_candidate.append(atom2)

        # 충돌 가능성이 있는 후보들 중 가장 먼저 충돌돌

    retur total_energy


T = int(input())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    N = int(input())  # 원자 수

    # ((x:x좌표, y:y좌표), d:이동방향, k:보유 에너지 )
    atoms = [list(map(int, input().rstrip().split())) for _ in range(N)]

    result = atom_extinction(atoms)

    print(f"#{tc} {result}")
