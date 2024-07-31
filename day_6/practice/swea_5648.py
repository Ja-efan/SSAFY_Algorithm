import sys

sys.stdin = open("../inputs/input_5648.txt")

from collections import defaultdict

T = int(input())

directions = {
    0: [0, 1],  # 상
    1: [0, -1],  # 하
    2: [-1, 0],  # 좌
    3: [1, 0]  # 우
}


def remove_elements(original_list, remove_index):
    """
    remove_elements() 함수는 original_list에서 remove_index 내 인덱스에 해당하는 원소를 삭제하는 함수
    :param original_list: 원본 리스트
    :param remove_index: 삭제할 원소 인덱스
    :return: 원소들을 제거한 리스트
    """
    # 인덱스를 내림차순으로 정렬
    remove_index.sort(reverse=True)

    # 새로운 리스트 생성
    result = original_list.copy()

    # 정렬된 인덱스를 순회하며 요소 제거
    for index in remove_index:
        if 0 <= index < len(result):
            result = result[:index] + result[index + 1:]

    return result


for tc in range(1, T + 1):
    N = int(input())  # 원자 개수
    # atoms 원소 구조 : [x: 초기 x 좌표, y: 초기 y 좌표, d: 이동 방향, k: 보유 에너지]
    atoms = [list(map(int, input().split())) for _ in range(N)]

    total_energy = 0
    # 충돌이 일어나지 않는다는 가정하에 예상 이동 시간(거리)가 가장 긴 원소의 이동시간 : max_time
    max_time = 0

    for atom in atoms:
        direction = atom[2]
        if direction == 0:  # 상
            tmp_time = 1000 - atom[1]
            max_time = max(max_time, tmp_time)
        elif direction == 1:  # 하
            tmp_time = -1000 - atom[1]
            max_time = max(max_time, abs(tmp_time))
        elif direction == 2:  # 좌
            tmp_time = 1000 - atom[0]
            max_time = max(max_time, tmp_time)
        elif direction == 3:  # 우
            tmp_time = -1000 - atom[0]
            max_time = max(max_time, abs(tmp_time))
        else:
            raise ValueError("원자의 방향 정보가 올바르지 않습니다.")

    step = 0.5
    time = 0.5
    # 최대 이동 시간동안 반복
    while time <= max_time:
        # 남은 원자가 존재하지 않는다면 while 문 종료
        if not atoms:
            break

        # 0.5초 마다 위치 갱신
        next_position_dict = defaultdict(list)  # 위치 정보 담을 딕셔너리
        for i in range(len(atoms)):  # 모든 원자에 대해 순회
            atom = atoms[i]  # 원자
            x, y, d = atom[0], atom[1], atom[2]  # 원자 좌표와 이동 방향(0 or 1 or 2 or 3)
            dx, dy = directions[d]  # x 및 y 방향에 대한 이동 방향
            nx, ny = x + dx * step, y + dy * step  # 원자의 다음 좌표
            atoms[i][0], atoms[i][1] = nx, ny  # 원자의 좌표 갱신

            next_position_dict[(nx, ny)].append(i)

        # 충돌한 원자 인덱스
        remove_index = [idx for indices in next_position_dict.values() if len(indices) > 1 for idx in indices]

        # 충돌한 원자가 있는 경우
        if remove_index:
            total_energy += sum(atoms[idx][-1] for idx in remove_index)  # 충돌한 원자의 에너지 방출 (누적 합)
            atoms = [atom for i, atom in enumerate(atoms) if i not in remove_index]  # 충돌한 원자를 제외한 원자 리스트 갱신

        time += step

    print(f"#{tc} {total_energy}")
