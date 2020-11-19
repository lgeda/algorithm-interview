
# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
# 대소문자 구분하지 않고, 구두점(마침표, 쉼표 등)은 무시한다.

import re
from collections import Counter

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
expected = "ball"

# 소문자로 바꿔
lowstr = paragraph.lower()
print(lowstr)

# 알파벳만 남겨
only_char_str = " ".join(re.findall("[a-zA-Z]+", lowstr))
only_char_str2 = re.sub('[^a-z0-9 ]','', lowstr)  # better

print("-")
print(only_char_str)
print(only_char_str2)
print("-")

# 금지단어 제거
for i in banned:
    remove_banned = only_char_str.replace(i, "")
print(remove_banned)

# 리스트 전환
word_list = remove_banned.split()
print(word_list)

# 카운터 사용
count = Counter(word_list)
print(count.most_common(1))
print(count.most_common(1)[0][0])



