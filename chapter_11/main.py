class Person:
    def __init__(self):
        print("Person:init is called")
        self.name = "Jack"


class Student(Person):
    def __init__(self):
        super().__init__()
        print("Student:init is called")
        self.school = "Abc"


class Stone:
    pass


def main():
    student = Student()
    print(student.name)
    print(student.school)

    print(isinstance(student, Student))
    print(isinstance(student, Person))

    person = Person()
    print(isinstance(person, Student))

    print(issubclass(Student, Person))
    print(issubclass(Person, Student))

    stone = Stone()
    print(issubclass(Stone, Student))
    print(isinstance(stone, Person))


if __name__ == '__main__':
    main()
