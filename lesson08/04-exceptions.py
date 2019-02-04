class UserRoleException(Exception):
    user_role: str
    user_action: str

    def __init__(self, user_role, user_action):
        super(UserRoleException, self).__init__()

        self.user_role = user_role
        self.user_action = user_action

    def __str__(self):
        return f"UserRoleException: Роль {self.user_role} не подходит для {self.user_action}"


class User:
    login: str
    role: int

    def hey(self):
        if self.role == 'admin':
            return f"{self.login}, role - {self.role}"
        else:
            raise UserRoleException(self.role, 'Hey method')


john = User()
john.login = 'john'
john.role = 'manager'

try:
    print(john.hey())
except UserRoleException as error:
    print('method not allowed', error.user_action)
