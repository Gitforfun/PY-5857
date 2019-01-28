class Behavior(object):
    name: str

    def __init__(self, name):
        self.name = name


class Animal(object):
    def walk(self):
        print('walking ...')


class Dog(Animal, Behavior):
    pass


class Cat(Animal):
    def walk(self):
        print('meoow')


doggy = Dog('unknown')
doggy.walk()

catty = Cat()
catty.walk()
