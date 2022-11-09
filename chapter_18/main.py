from chapter_18.student_1 import Student1
from chapter_18.student_2 import Student2


def main():
    student_1 = Student1("Jack", "Ma")
    # student_1.last_name = ""

    student_2 = Student2()
    student_2.first_name = "Jack"  #first_name.__set__(student_2, "Jack")
    student_2.last_name = "Ma"

    student_3 = Student2()
    student_3.first_name = "   Tom"
    student_3.last_name = "Li"

    print(student_2.first_name)
    print(student_3.first_name)


if __name__ == '__main__':
    main()
