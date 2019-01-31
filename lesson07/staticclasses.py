class Global:
    objects = []
    INDEX = 0

    # def __init__(self):
    #     Global.objects +=

    def increment(self):
        self.INDEX += 1

    @staticmethod
    def show_message():
        print('CLASS STATIC METHOD')

    # @staticmethod
    # def convert_string(value: str):
    #     return value.upper()

    @classmethod
    def increments(cls):
        cls.INDEX += 1


a = Global()
a.increment()
print(a.INDEX)

b = Global()
print(b.INDEX)

b.show_message()
Global.show_message()

Global.increments()
b.increments()
print(b.INDEX)
