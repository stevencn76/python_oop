from chapter_18.required_string import RequiredString


class Student2:
    first_name = RequiredString(True)
    last_name = RequiredString(True)
    password = RequiredString(False)
