nums = [1, 2, 3, 4]

# for x in nums:
#     print(x * 2)

print(list(map(lambda x: x * 2, nums)))
# print(list(reduce(lambda x, y: x * 2, nums)))

num2 = ['01', '02', '03']
print(list(map(int, num2)))

my_lambda = lambda x: x * 2
my_lambda(100)
print(type(my_lambda))