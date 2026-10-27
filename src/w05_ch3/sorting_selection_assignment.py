import random

ARRAY_SIZE = 30
randomizer = random.Random("EX_03")

def merge_sort(array):
    """array를 오름차순으로 직접 정렬한다."""
    # 함수는 새 정렬 결과를 반환하지 않고, 전달받은 array를 직접 정렬해야 한다.
    merge_sort_range(array, 0, len(array) - 1)
    return array

def merge_sort_range(array, left, right):
    """array의 left..right 구간을 오름차순으로 직접 정렬한다."""
    # left와 right index를 모두 포함한다. 빈 구간은 left > right이다.
    if left >= right:
        return

    mid = (left + right) // 2
    # 왼쪽은 left..mid, 오른쪽은 mid+1..right이며 각 끝 index를 포함한다.
    merge_sort_range(array, left, mid)
    merge_sort_range(array, mid + 1, right)
    merge(array, left, mid, right)

def merge(array, left, mid, right):
    """array의 left..mid와 mid+1..right 구간을 병합한다."""
    # left, mid, right를 모두 포함한다. mid는 왼쪽 구간의 마지막 index이다.
    # 슬라이스는 끝 index를 제외하므로 mid + 1, right + 1까지 지정한다.
    left_array = array[left:mid + 1]
    right_array = array[mid + 1:right + 1]

    i, j, k = 0, 0, left

    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1

def quick_sort(array):
    """array를 오름차순으로 직접 정렬한다."""
    # 함수는 새 정렬 결과를 반환하지 않고, 전달받은 array를 직접 정렬해야 한다.
    if len(array) > 0:
        quick_sort_range(array, 0, len(array) - 1)

    return array

def quick_sort_range(array, left, right):
    """array의 left..right 구간을 오름차순으로 직접 정렬한다."""
    # left와 right index를 모두 포함한다. 빈 구간 또는 원소 하나면 종료한다.
    if left >= right:
        return

    pivot_index = partition(array, left, right)

    # pivot_index는 확정된 위치이므로 제외한다. 각 재귀 구간의 양 끝은 포함한다.
    quick_sort_range(array, left, pivot_index - 1)
    quick_sort_range(array, pivot_index + 1, right)

def selection(array, n):
    """array에서 n번째로 작은 값을 반환한다. n은 1부터 시작한다."""
    # partition 과정에서 array의 원소 위치가 바뀌어도 된다.

    if not 1 <= n <= len(array):
        raise ValueError("n은 배열 길이 안의 1 이상인 값이어야 합니다.")

    return selection_range(array, 0, len(array) - 1, n)

def partition(array, left, right):
    """array의 left..right 구간을 partition하고, pivot의 최종 index를 반환한다."""
    # left와 right index를 모두 포함한다. randint도 양 끝 index를 포함한다.
    pivot_index = randomizer.randint(left, right)
    array[left], array[pivot_index] = array[pivot_index], array[left]
    pivot = array[left]
    i = left + 1
    j = right

    while True:
        while i <= j and array[i] <= pivot:
            i += 1
        while i <= j and array[j] >= pivot:
            j -= 1
        if i > j:
            break
        array[i], array[j] = array[j], array[i]

    array[left], array[j] = array[j], array[left]
    # 반환하는 j는 pivot의 확정 index이다. left <= j <= right이다.
    # left..j-1은 pivot 이하, j+1..right는 pivot 이상이며 각 끝 index를 포함한다.
    return j

def selection_range(array, left, right, n):
    """array의 left..right 구간에서 n번째로 작은 값을 반환한다. n은 1부터 시작한다."""
    # left와 right index를 모두 포함한다. n은 현재 구간 안에서의 1부터 시작하는 순위이다.
    if left == right:
        return array[left]

    # Quick Sort와 같은 partition을 호출하고, 필요한 한쪽 구간만 탐색한다.
    pivot_index = partition(array, left, right)
    pivot_rank = pivot_index - left + 1

    if n == pivot_rank:
        return array[pivot_index]
    elif n < pivot_rank:
        # left..pivot_index-1의 양 끝 index를 포함하며 pivot은 제외한다.
        return selection_range(array, left, pivot_index - 1, n)
    else:
        # pivot_index+1..right의 양 끝 index를 포함하며 제외한 원소 수만큼 순위를 줄인다.
        return selection_range(array, pivot_index + 1, right, n - pivot_rank)


def make_random_array(randomizer):
    """1부터 99 사이의 값 ARRAY_SIZE 개를 가진 새 배열을 만든다."""
    # range(ARRAY_SIZE)는 0..ARRAY_SIZE-1이며 끝값 ARRAY_SIZE를 포함하지 않는다.
    return [randomizer.randint(1, 99) for _ in range(ARRAY_SIZE)]




if __name__ == "__main__":
    randomizer = random.Random()
    # 정렬 두 개는 서로 다른 무작위 배열을 사용한다.
    merge_data = make_random_array(randomizer)
    quick_data = make_random_array(randomizer)

    print("Merge Sort")
    print("정렬 전:", merge_data)
    merge_sort(merge_data)
    print("정렬 후:", merge_data)
    print()

    print("Quick Sort")
    print("정렬 전:", quick_data)
    quick_sort(quick_data)
    print("정렬 후:", quick_data)
    print()

    # Selection은 별도의 30개 배열에서 10~24 사이에서 뽑은 두 순위를 찾는다.
    selection_data = make_random_array(randomizer)
    first_n = randomizer.randint(10, 24)
    second_n = randomizer.randint(10, 24)

    print("Selection")
    print("배열:", selection_data)
    print(f"{first_n}번째로 작은 값은:", selection(selection_data, first_n))
    print(f"{second_n}번째로 작은 값은:", selection(selection_data, second_n))
