# 가장 긴 팰린드롬 부분 문자열을 출력하라.
#
# 입력
# "babad"
#
# 출력
# "bab" or "aba"


def palindrom(string: str) -> bool:
    ll: int = 0
    r: int = len(string)-1
    while(ll < r):
        if string[ll] != string[r]:
            return False
        ll = ll + 1
        r = r - 1

    return True


def f(string: str) -> str:
    for i in range(len(string), 0, -1):
        for j in range(1+len(string)-i):
            if palindrom(string[j:i+j:1]):
                return string[j:i+j:1]


def f2(string: str) -> str:
    def palindrom(ll, r):
        while(ll < r):
            if(string[ll] != string[r]):
                return False
            ll += 1
            r -= 1
        return True

    for i in range(len(string), 0, -1):
        for j in range(1+len(string)-i):
            if(palindrom(j, i+j-1)):
                return string[j:i+j]


def f3(string: str) -> str:
    def expand(ll, r):
        while ll >= 0 and r <= len(string) and string[ll] == string[r-1]:
            ll -= 1
            r += 1
        return string[ll+1:r-1]

    if len(string) < 2 or string == string[::-1]:
        return string

    result = ''
    for i in range(len(string)-1):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)

    return result


if __name__ == "__main__":
    data = "babad"
    print(f(data))
    print(f2(data))
    print(f3(data))
