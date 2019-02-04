import json

json_input = '{"users":[{"login":"admin","password":"root","role":1},{"login":"manager","password":"root","role":2}]}'


class User:
    login: str
    password: str
    role: int

    def __init__(self, dictionary):
        for key, value in dictionary.items():
            setattr(self, key, value)

    @staticmethod
    def factory(json_input):
        data = json.loads(json_input)
        users = []
        for x in data['users']:
            u = User(x)

            # for key, value in x.items():
            #     setattr(u, key, value)

            users.append(u)
        return users


users = User.factory(json_input)
print(users)
