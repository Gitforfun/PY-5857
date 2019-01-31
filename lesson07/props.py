class Person:
    first_name: str
    last_name: str

    _age: int = 0
    __test = 10

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self):
        return f'{self._age} лет'

    @age.setter
    def age(self, value):
        if value < 130 and value > 0:
            self._age = value
        else:
            print('invalid age')

    def __str__(self):
        return self.full_name

john = Person()
john.first_name = 'John'
john.last_name = 'Doe'
john.age = 300

print(john._age)

print(john)
print(john.age)

print(john._Person__test)
