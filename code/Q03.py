# 1. 로그의 가장 앞 부분은 식별자다.
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순서대로 한다.
#
# 입력
# logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
#
# 출력
# ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
#


def insertsort(alogs: list, log: str) -> None:
    index: int = 0
    str1: str
    str2: str
    for alog in alogs:
        str1 = " ".join(alog.split()[1:])
        str2 = " ".join(log.split()[1:])
        if(str1 < str2):
            index = index + 1
        elif str1 == str2:
            if (str1.split()[0] < str2.split()[0]):
                pass
            else:
                index = index+1
            break
        else:
            break
    alogs.insert(index, log)


def arrange(logs: list) -> list:
    alogs = []
    nlogs = []
    for log in logs:
        if(log.split()[1].isnumeric()):
            nlogs.append(log)
        else:
            insertsort(alogs, log)
    return alogs + nlogs


def arrange2(logs: list) -> list:
    alogs = []
    nlogs = []
    for log in logs:
        if(log.split()[1].isnumeric()):
            nlogs.append(log)
        else:
            alogs.append(log)

    alogs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return alogs + nlogs


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig",
            "let3 art zero", "let4 art zero"]
    print(logs)
    print(arrange(logs))
    print(arrange2(logs))
