class salary(float):
    def __str__(self):
        temp = salary(round(self, 2))
        result = super(salary, temp).__str__()
        return f'{result} руб'

    # def custom_format(self):


a = float(4.123123)
b = salary(4.123123)

print(a)
print(b)

print(type(a))
print(type(b))
