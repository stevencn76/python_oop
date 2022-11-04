class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age: int):
        if age < 0 or age > 200:
            raise Exception(f"Age {age} is not valid")
        self.__age = age

    def __str__(self):
        return f"{self.name}, {self.__age}"

    age = property(fget=get_age, fset=set_age)


def main():
    student = Student("Jack", 18)
    student.age = 3
    print(student.age)
    student.set_age(3)
    print(student.get_age())


if __name__ == '__main__':
    main()
