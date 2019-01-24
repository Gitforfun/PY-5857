number = [4, 8, 15, 16]


# for x in number:
#     x = x + 1
#     print(x)
#
# print(number)
#
# for x in number.copy():
#     number.remove(x)
#
# print(number)


def test(my_list: list):
    a = my_list[:]
    a.remove(4)
    print(a)


test(number)
print(number)
