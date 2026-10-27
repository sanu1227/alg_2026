import pyvisalgo as va

import ch3_2_quick_sort as qs


DATA_FILE = "data/selection.json"

vis = va.visualizer("selection")


def selection(array, rank):
    """array에서 rank번째로 작은 값을 찾는다. rank는 1부터 시작한다."""
    if not 1 <= rank <= len(array):
        raise ValueError("rank는 배열 길이 안의 1 이상인 값이어야 합니다.")

    # 첫 탐색 범위는 배열 전체입니다.
    return selection_range(array, 0, len(array) - 1, rank)


def selection_range(array, left, right, rank):
    """array[left..right]에서 rank번째로 작은 값을 찾는다. right도 포함한다."""
    # 재귀 depth마다 현재 남은 범위와, 그 안에서 찾을 상대 순위를 기록합니다.
    vis.push(left, right, rank)

    # Quick Sort와 같은 방식으로 pivot을 골라 현재 범위를 양쪽으로 나눕니다.
    # Selection은 이 뒤에 답이 있는 한쪽만 남기는 점이 Quick Sort와 다릅니다.
    pivot_index = qs.partition_random(array, left, right)

    # pivot의 배열 전체 index가 아니라, 현재 범위 안에서 몇 번째인지 계산합니다.
    pivot_rank = pivot_index - left + 1
    vis.show_pivot_rank(pivot_index, rank)

    # 현재 범위에서 pivot이 찾는 순위와 같으면, 이 값이 바로 답입니다.
    if rank == pivot_rank:
        vis.found(pivot_index, rank)
        return array[pivot_index]

    # 찾는 순위가 pivot보다 앞이면, pivot 오른쪽은 보지 않고 왼쪽에서 같은 순위를 찾습니다.
    if rank < pivot_rank:
        vis.keep_left(pivot_index, rank)
        return selection_range(array, left, pivot_index - 1, rank)

    # pivot과 그 왼쪽에는 pivot_rank개의 작은 값이 있으므로,
    # 오른쪽 범위에서는 그 수를 뺀 순위를 다시 찾습니다.
    next_rank = rank - pivot_rank
    vis.keep_right(pivot_index, next_rank)
    return selection_range(array, pivot_index + 1, right, next_rank)


if __name__ == "__main__":
    while va.running():
        data = va.next_data(__file__, data_file=DATA_FILE)
        array = list(data.array)
        original = list(array)

        # Quick Sort 모듈의 partition도 현재 Selection visualizer에 그리도록 연결합니다.
        qs.vis = vis
        vis.setup(data)
        print("선택 전:", array)
        print(f"찾을 순위: {data.n}번째")
        value = selection(array, data.n)
        print(f"{data.n}번째 작은 값:", value)
        print("정렬했을 때의 확인 값:", sorted(original)[data.n - 1])
        vis.wait()
