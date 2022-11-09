class RequiredString:
    def __init__(self, trim: bool):
        self.__trim = trim

    def __set_name__(self, owner, name):
        self.__property_name = name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise Exception(f"{self.__property_name} is not a string")

        value = value.strip()
        if len(value) == 0:
            raise Exception(f"{self.__property_name} is empty")

        instance.__dict__[self.__property_name] = value

    def __get__(self, instance, owner):
        if self.__property_name in instance.__dict__:
            return instance.__dict__[self.__property_name]

        return None
