# 문자열을 받아서 애너그램 단위로 그룹핑 하라

input = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = [
            ["ate", "eat", "tea"],
            ["nat", "tan"],
            ["bat"]
         ]

# 머리속 풀이
# 각 문자열을 소팅한 후에 같은 것 끼리 묶음 -> 소팅한 문자열을 Key로 하고 같은 그룹의 문자열 리스트를 Value 만들면 될 듯

output_dict = {}  # declare dict

for i in input:
    # print(i)
    key_str = ''.join(sorted(i))  # 1. 키 만들기
    # print(key_str)

    if key_str in output_dict:  # 2. 키에 해당하는 값으로 빈 리스트 만들기. 이미 있다면 만들지 않기
        # print("exist key")
        pass
    else:
        # print("no key")
        output_dict[key_str] = list()

    output_dict[key_str].append(i)  # 3. 같은 키 값을 같은 문자열 추가하기
    # print(output_dict[key_str])
    # print(output_dict)


output_list = list()
for i in output_dict.values():
    i.sort()  # 소팅하고
    output_list.append(i)  # 리스트의 리스트 만들기

print(output_list)
print(list(output_dict.values()))




