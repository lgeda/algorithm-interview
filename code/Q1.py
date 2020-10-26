import collections
import re

def isPalindrome1(s:str) -> bool:
    ss = []
    for c in s:
        if( c.isalnum() ):
            ss.append(c.lower())

    for i in range(0, len(ss)//2):
        if ss[i] != ss[len(ss)-1-i]:
            return False
    return True

def isPalindrome2(s:str) -> bool:
    ss = []
    for c in s:
        if( c.isalnum() ):
            ss.append(c.lower())

    while( len(ss) > 1): 
        if( ss.pop(0) != ss.pop()):
            return False
    return True

def isPalindrome3(s:str) -> bool:
    ss = collections.deque()
    for c in s:
        if( c.isalnum() ):
            ss.append(c.lower())

    while( len(ss) > 1): 
        if( ss.popleft() != ss.pop()):
            return False
    return True

def isPalindrome4(s:str) -> bool:
    ss = re.sub('[^a-z0-9]','',s.lower())
    return ss == ss[::-1]

if __name__ == "__main__":
	print(isPalindrome1("A man, a plan, a canal: Panama"))
	print(isPalindrome1("race a car"))

	print(isPalindrome2("A man, a plan, a canal: Panama"))
	print(isPalindrome2("race a car"))

	print(isPalindrome3("A man, a plan, a canal: Panama"))
	print(isPalindrome3("race a car"))

	print(isPalindrome4("A man, a plan, a canal: Panama"))
	print(isPalindrome4("race a car"))
