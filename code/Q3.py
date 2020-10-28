# Re-sort logs -> 문제를 이해 못하겠음
# 맨앞 dig1 같은 것은 식별자다. 문자로만 되어있는 것이 우선이다. 식별자는 순서에 영향 없다.
# 문자가 동일하면 식별자 순으로 한다.(..."let1 art can", "let3 art zero",...)
# 숫자 로그는 입력 순을 유지 한다.

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]

resorted_logs = ["let1 art can", "let3 art zero", "let2 own kit dig",
                 "dig1 8 1 5 1", "dig2 3 6"]


for i in logs:
    logs2 = i.split()
    logs2.pop(0)
    print(logs2)

# 쩝, 문제를 이해 못해서 못풀겠음


