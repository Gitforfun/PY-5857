# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [
#         [10, 20]
#     ],
# ]
#
# m_sum = 0
#
# for x in matrix:
#     for y in x:
#         m_sum += y
#
# print(m_sum)

a = ["A", "B", "C"]
b = ['first', 'second', [3, 'third']]

# c = list(zip(a, b))
c = {key: value for key, value in zip(a, b)}

print(c['A'])
