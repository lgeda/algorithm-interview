print("hello")

for i in range(1, 10):
    print(i)    # 재밌어?

a: str = 1
print(type(a))


print([n * 2 for n in range(1, 10 + 1) if n % 2 == 1])


def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n


a = get_natural_number()

print(a)

for i in range(0, 10):
    print(next(a))


