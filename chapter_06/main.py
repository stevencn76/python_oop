class MyDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        print("str is called")
        return f"{self.year}-{self.month}-{self.day}"

    def __repr__(self):
        print("repr is called")
        return f"MyDate:{self.year}-{self.month}-{self.day}"

    def __eq__(self, other):
        print("eq is called")
        if not isinstance(other, MyDate):
            return False

        return self.year == other.year \
               and self.month == other.month \
               and self.day == other.day

    def __hash__(self):
        print("hash is called")
        return hash(self.year + self.month * 101 + self.day * 101)

    def __bool__(self):
        print("bool is called")
        return self.year > 2021

    def __del__(self):
        print("del is called")


def main():
    my_date_1 = MyDate(2022, 11, 3)
    my_date_2 = MyDate(2022, 11, 3)
    my_date_5 = MyDate(2020, 1, 1)
    my_date_3 = my_date_1
    print(my_date_1)
    print(repr(my_date_1))

    my_date_5 = None

    print(my_date_1 is my_date_3)
    print(my_date_1 == my_date_2)

    date_set = set()
    date_set.add(my_date_1)
    print(hash(my_date_1))

    my_date_4 = MyDate(2020, 2, 1)
    print(bool(my_date_1))
    print(bool(my_date_4))


if __name__ == '__main__':
    main()
