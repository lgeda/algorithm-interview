
input_list = ["h", "e", "l", "l", "o"]
expect_list = ["o", "l", "l", "e", "h"]


def reverse_list(l) -> list:
    ret_list = list()
    reverse_string = ''.join(l)[::-1]  # list -> str, 반대는 어떻게?
    # print(reverse_string)
    for ch in reverse_string:
        ret_list.append(ch)
    # print(ret_list)
    return ret_list


def reverse_list_noreturn(l) -> None:
    print("input:{}".format(l))
    for i in range(0, len(l)//2 + 1):
        temp = l[len(l)-1-i]
        l[len(l)-1-i] = l[i]
        l[i] = temp
    print("output:{}".format(l))


def reverse_list1(l) -> None:
    print("input:{}".format(l))
    left, right = 0, len(l) - 1
    while left < right:
        l[left], l[right] = l[right], l[left]
        # swap을 위한 temp가 필요없는건가?
        left += 1
        right -= 1
    print("output:{}".format(l))


def reverse_list2(l) -> None:
    print("input:{}".format(l))
    l.reverse()
    print("output:{}".format(l))


def reverse_list3(l) -> None:
    print("input:{}".format(l))
    l[:] = l[::-1]  # l = l[::-1]은 모호하다는 경고가 뜬다
    print("output:{}".format(l))


if __name__ == "__main__":
    print(reverse_list(input_list) == expect_list)
    print()

    reverse_list_noreturn(input_list)
    print()

    reverse_list1(input_list)
    print()

    reverse_list2(input_list)
    print()

    reverse_list3(input_list)
    print()
