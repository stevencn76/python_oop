
class Student:
    def __init__(self, name: str):
        self.__name = name

    def __say_hello(self, msg: str):
        print(f"Hello {msg}, {self.__name}")


def main():
    s1 = Student("Jack")
    print(s1._Student__name)   # _classname__attribute

    s1._Student__say_hello("1111")


if __name__ == '__main__':
    main()
