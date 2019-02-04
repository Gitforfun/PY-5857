class Singleton:
    instance = None

    # TODO
    class __singleton:
        def __init__(self):
            self.value = None

    @classmethod
    def __new__(cls):
        if cls.instance is not None:
            cls.instance = cls.__singleton()

        return cls.instance

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr__(self, key, value):
        return setattr(self.instance, key, value)
