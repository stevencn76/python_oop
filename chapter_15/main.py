import enum
from enum import Enum


class Status(Enum):
    SUCCESS = 1
    OK = 1
    FAIL = 2
    WRONG = 2


@enum.unique
class Gender(Enum):
    MALE = 1
    FEMALE = 2


def main():
    for s in Status:
        print(s.name)

    print(Status.__members__)

    print(Status.SUCCESS == Status.OK)
    print(Status.SUCCESS is Status.OK)


if __name__ == '__main__':
    main()
