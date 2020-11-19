# 빗물 트래핑
# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라
# 입력
# [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# 출력
# 6


def f(data: list) -> int:
    max_index = data.index(max(data))
    sum = 0
    left: int = 0
    lmax: int = data[0]
    while(left < max_index):
        sum += max(0, lmax - data[left])
        lmax = max(lmax, data[left])
        left += 1
    right: int = len(data) - 1
    rmax: int = data[right]
    while(right > max_index):
        sum += max(0, rmax - data[right])
        rmax = max(rmax, data[right])
        right -= 1
    return sum


if __name__ == "__main__":
    data = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f(data))
