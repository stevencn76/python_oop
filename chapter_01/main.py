class Student:
    pass


class Person:
    pass


def main():
    print(type(Student))
    print(type(Person))
    print(isinstance(Student, type))

    print(Student)

    student_1 = Student()
    print(isinstance(student_1, Person))

    print(student_1)

    student_1 = Student()

    print(student_1)
    print(hex(id(student_1)))


if __name__ == '__main__':
    main()
