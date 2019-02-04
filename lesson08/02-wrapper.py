class User:
    login: str
    role: int

    def hey(self):
        return f"{self.login}, role - {self.role}"


class UserWrapper:
    def __init__(self, object: User):
        self.wrapped_object = object

    def __getattr__(self, item):
        print(f"Requested: {item}")

        if self.wrapped_object.role == 'admin':
            return getattr(self.wrapped_object, item)
        else:
            return self.none_answer

    def none_answer(self):
        return None


john = User()
john.login = 'john'
john.role = 'manager'

print(john.hey())

wrapper = UserWrapper(john)
print(wrapper.hey())
