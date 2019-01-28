# employees = [
#     {
#         'name': 'John',
#         'job': 'Director',
#         'salary': 100,
#     },
#     {
#         'name': 'Artur',
#         'job': 'Director',
#         'salary': 100,
#     }
# ]
#
#
# def show_employees(employees):
#     for emp in employees:
#         "Employee {}, salary {}".format(
#             emp['name'],
#             emp['salary'] - (emp['salary'] * 0.13)
#         )


class Employee(object):
    name: str
    job: str
    _salary_main: int

    def __init__(self, first_name):
        self.name = first_name

    def __str__(self):
        return f'Employee: {self.name}'

    def __repr__(self):
        return self.__str__()

    def set_title(self, job_title, salary_size):
        self.job = job_title
        self._salary_main = salary_size

    def info(self):
        return f"{self.name}, {self.salary_main} EUR"

    @property
    def salary_main(self):
        return f'{self._salary_main} EUR'

    @salary_main.setter
    def salary_main(self, value):
        self._salary_main = value - (value * 0.3)


john = Employee('John')
john.set_title('Developer', 450)

arty = Employee('Artur')
arty.set_title('Designer', 450)

employees = [john, arty]
print(employees)
