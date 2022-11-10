class InvalidArgumentException(Exception):
    def __init__(self, *args):
        super().__init__(args)


def add(n1, n2):
    if not isinstance(n1, int) or not isinstance(n2, int):
        raise InvalidArgumentException("Argument is not int")

    return n1 + n2


def main():
    try:
        num = 2
        s = 10
        res = num / s

        print(res)

        names = ("Jack", "Tom")
        print(names[0])

        add("a", "b")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except InvalidArgumentException as iae:
        print(f"Argument is not valid: {iae}")
    except Exception as ex:
        print(f"Exception: {ex}")


if __name__ == '__main__':
    main()
