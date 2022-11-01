from pprint import pprint


class Student:
    def __init__(self, name: str):
        self.name = name

    def say_hello(self, msg: str):
        print(f"Hello {msg}, {self.name}")


def main():
    # 1. create a physical object
    # 2. call __init__() to initialize this object
    s1 = Student("Jack")
    s2 = Student("Tom")

    s1.say_hello("1111")
    s2.say_hello("2222")

    s1.gender = 'Male'
    print(s1.gender)
    print(s2.gender)


if __name__ == '__main__':
    main()
