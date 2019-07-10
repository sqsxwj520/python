
def fn(name: str):
    def wrapper(cls):
        cls.NAME = name
        return cls
    return wrapper


@fn('abc')
class Person:
    pass


print(Person.__dict__)
