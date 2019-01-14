name = "artur"
# type(name)  # <class 'str'>
print(name.capitalize())
print(name.upper())
print(name.isupper())

name.count('r')  # кол-во вхождений
len(name)  # длина

age = 15
name = "My name is {0} and age = {1}, {0}".format('Artur', age)
name = f"My name is {name} and age = {age}, {name}"

a_letter = ord("a")
b_letter = chr(98)
print(a_letter)
print(b_letter)

print("Number: %d and Character: %s" % (a_letter, b_letter))

title = "this is python"
# title = [1,2,3,4,5]
print(title[0])
print(title[-1])
print(title[0:4])
print(title[0:4:2])
print(title[::-1])
