
input = "a man, a nA"
input2 = "aba"


def check_p(input):
    check_str = list()
    for i in input:
        if i.isalnum():
            check_str.append(i.lower())  # amanana

    revers_str = check_str.copy()
    revers_str.reverse()

    print('r:{},c:{}'.format(revers_str, check_str))
    if revers_str == check_str:
        return True
    return False


print(check_p(input))
print(check_p(input2))
