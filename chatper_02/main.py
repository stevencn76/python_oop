from pprint import pprint


class Student:
    student_count = 8


def main():
    print(Student.__name__)

    print(Student.student_count)
    print(getattr(Student, "student_count"))
    # print(Student.unknown)
    print(getattr(Student, "unknown", "10"))

    Student.student_count = 89
    setattr(Student, "student_count", 100)
    print(Student.student_count)

    Student.newattribute = "hello"
    print(Student.newattribute)

    # del Student.newattribute
    delattr(Student, "newattribute")
    # print(Student.newattribute)

    s1 = Student()
    s2 = Student()
    Student.student_count = 4
    print(s1.student_count)
    print(s2.student_count)

    pprint(Student.__dict__)


if __name__ == '__main__':
    main()
