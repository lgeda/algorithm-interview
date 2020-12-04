# 1. 입력받아서 알파벳과 숫자만 리스트에 저장
# 2. 루프- i=0부터 n/2까지 돌면서 n-i가 i랑 같은지 확인
# 3. 다르면 false로 나가기. 끝나면 true


def isPalindrome1(s):
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


print(isPalindrome1("A man, a plan, a canal: Panama"))
