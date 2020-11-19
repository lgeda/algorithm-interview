# 세 수의 합
# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라
# 입력
# nums = [-1, 0, 1, 2, -1, -4]
# 출력
# [ [-1, 0, 1], [-1, -1, 2] ]


def f(nums: list) -> list:
    result = []
    if len(nums) < 3:
        return None
    i, j, k = 0, 0, 0
    while(i < len(nums)):
        j = i + 1
        while(j < len(nums)):
            k = j + 1
            while(k < len(nums)):
                if(nums[i] + nums[j] + nums[k] == 0):
                    if(sorted([nums[i], nums[j], nums[k]]) not in result):
                        result.append(sorted([nums[i], nums[j], nums[k]]))
                k += 1
            j += 1
        i += 1
    return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(f(nums))
