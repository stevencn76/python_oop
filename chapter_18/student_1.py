class Student1:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        if not isinstance(first_name, str):
            raise Exception("First name is not a string")

        if len(first_name) == 0:
            raise Exception("First name is empty")

        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        if not isinstance(last_name, str):
            raise Exception("Last name is not a string")

        if len(last_name) == 0:
            raise Exception("Last name is empty")

        self.__last_name = last_name
