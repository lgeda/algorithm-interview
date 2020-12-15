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


def f2(nums: list) -> list:
    result = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i + 1, len(nums)-1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append((nums[i], nums[left], nums[right]))
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(f(nums))
    print(f2(nums))
