# @staticmethod -> staticmethod(Settings)


def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()

        print(instances)

        return instances[cls]

    return get_instance


@singleton  # singleton(Settings) -> get_instance
class Settings:
    host: str
    database: str

    def show_connection(self):
        print(f"Host: {self.host}, database: {self.database}")


sets1 = Settings()
sets1.host = 'localhost'
sets1.database = 'geek-db'

sets2 = Settings()
# sets2.host = '127.0.0.1'
# sets2.database = 'test-geek-db'

sets1.show_connection()
sets2.show_connection()
