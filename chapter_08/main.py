class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if age < 0 or age > 200:
            raise Exception(f"Age {age} is not valid")
        self.__age = age

    def __str__(self):
        return f"{self.name}, {self.__age}"


def main():
    student = Student("Jack", 18)
    student.age = -3
    print(student.age)


if __name__ == '__main__':
    main()
