# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라
# 입력: [1, 2, 3, 4]
# 출력: [24, 12, 8, 6]
# 조건: 나눗셈을 하지 않고 O(n)에 풀이하라
from functools import reduce


def func1(input: list) -> list:
    temp = list()
    ret = list()

    for i in range(len(input)):
        # 해당 인덱스 값을 제거한 배열을 만들고
        temp.append(input.copy())
        del temp[i][i]

        # 만든 배열 값 요소를 곱해서 리턴함
        sum = 1
        for j in range(len(temp[i])):
            sum = sum * temp[i][j]
        ret.append(sum)

    print(ret)
    return ret


def func2(input: list) -> list:
    temp = list()
    ret = list()

    for i in range(len(input)):
        # 해당 인덱스 값을 제거한 배열을 만들고
        temp.append(input.copy())
        del temp[i][i]

        # 만든 배열 값 요소를 곱해서 리턴함
        # https://shoark7.github.io/programming/algorithm/3ways-to-get-multiplication-in-a-list-in-python
        ret.append(reduce(lambda x, y: x * y, temp[i]))

    print(ret)
    return ret


input = [1, 2, 3, 4]
expected = [24, 12, 8, 6]

print(func1(input) == expected)
print(func2(input) == expected)
