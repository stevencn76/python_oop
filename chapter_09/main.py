class Square:
    def __init__(self, width):
        self.__width = width
        self.__area = None

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.__width * self.__width

        return self.__area


def main():
    square = Square(5)
    print(square.area)
    square.width = 6
    print(square.area)


if __name__ == '__main__':
    main()
