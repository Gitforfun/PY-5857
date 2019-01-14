numbers = [4, 8, 15, 16, 23, 42]
# numbers.append('108')
numbers += ['108', 108]
numbers += [10]
# numbers = numbers + ['108', 108]

numbers.reverse()

a = numbers.copy()
b = list(numbers)

print(numbers)
