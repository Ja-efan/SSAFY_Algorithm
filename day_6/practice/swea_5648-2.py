import sys

sys.stdin = open("../inputs/input_5648.txt")

T = int(input())

directions = {
    0: [0, 1],  # 상
    1: [0, -1],  # 하
    2: [-1, 0],  # 좌
    3: [1, 0]  # 우
}


def atom_collision(atoms):
    return


def delete_element(arr, index):
    arr[index] = arr[-1]
    arr.pop()
    return arr


for tc in range(1, T + 1):
    N = int(input())  # 원자 개수
    # atoms 원소 구조 : [x: 초기 x 좌표, y: 초기 y 좌표, d: 이동 방향, k: 보유 에너지]
    atoms = [list(map(int, input().rstrip().split())) for _ in range(N)]

    total_energy = 0
    # 충돌이 일어나지 않는다는 가정하에 예상 이동 시간(거리)가 가장 긴 원소의 이동시간 max_time
    max_time = 0
    for atom in atoms:
        direction = atom[2]
        if direction == 0:  # 상
            tmp_time = 1000 - atom[1]
            max_time = max(max_time, tmp_time)
        elif direction == 1:  # 하
            tmp_time = -1000 - atom[1]
            max_time = max(max_time, tmp_time)
        elif direction == 2:  # 좌
            tmp_time = 1000 - atom[0]
            max_time = max(max_time, tmp_time)
        elif direction == 3:  # 우
            tmp_time = -1000 - atom[0]
            max_time = max(max_time, tmp_time)
        else:
            raise ValueError("원자의 방향 정보가 올바르지 않습니다.")
    step = 0.5
    time = 0.5
    while time <= max_time:
        # 0.5초 마다 위치 갱신
        next_position_dict = dict()  # 위치 정보 담을 딕셔너리
        for i in range(len(atoms)):  # 모든 원자에 대해 순회
            atom = atoms[i]
            x, y, d = atom[0], atom[1], atom[2]
            dx, dy = directions[d]
            nx, ny = x + dx*step, y + dy*step
            atoms[i][0], atoms[i][1] = nx, ny
            if (nx, ny) in next_position_dict.keys():  # 해당 좌표가 키로 존재하는 경우
                next_position_dict[(nx, ny)].append(i)
            else:  # 해당 좌표가 키로 존재하지 않는 경우
                next_position_dict[(nx, ny)] = [i]

        for v in next_position_dict.values():
            if len(v) > 1:
                for atom_idx in v:
                    total_energy += atoms[atom_idx][-1]
                    # 원소 하나를 지우면 길이가 바로바로 줄어들어서 다음 원자의 인덱스가 유효하지 않게 된다.
                    atoms = delete_element(atoms, atom_idx)

        time += 0.5

    print(f"#{tc} {total_energy}")