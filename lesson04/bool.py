a = 100
b = 40
c = 101

# print(a, b)
# print(bool(-1))

if a > 10 or (b > 10 and c == 100):  # && -> and    || -> or
    print('OK')
else:
    print('not OK')

print('OK' if a == 100 or b == 100 else 'not OK')
