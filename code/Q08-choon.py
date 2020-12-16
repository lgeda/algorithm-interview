# 문제: 빗물트래핑
# 해결: 모르겠다.


def debug(message, value):
    print('{}: {}'.format(message, value))


def func1(height_list):
    water_size = 0  # 저장된 물
    left_index, right_index = 0, len(height_list) - 1  # 왼쪽과 오른쪽에서 탐색을 시작

    # 왼쪽, 오른쪽 최대 높이 저장
    left_max, right_max = height_list[left_index], height_list[right_index]

#    debug("water_size", water_size)
#    debug("left_index", left_index)
#    debug("left_max", left_max)
#    debug("right_index", right_index)
#    debug("right_max", right_max)

    while left_index < right_index:
        left_max = max(height_list[left_index], left_max)
        right_max = max(height_list[right_index], right_max)

        if left_max <= right_max:  # 오른쪽이 높으면 왼쪽을 이동
            water_size += left_max - height_list[left_index]
            left_index += 1
        else:  # 왼쪽이 높으면 오른쪽을 이동
            water_size += right_max - height_list[right_index]
            right_index -= 1

    return water_size


input_list = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(func1(input_list) == 6)

