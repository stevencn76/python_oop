import enum
from enum import Enum
from functools import total_ordering


@enum.unique
class Gender(Enum):
    MALE = 1
    FEMALE = 2

    def __str__(self):
        return f"{self.name}({self.value})"

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other

        if isinstance(other, str):
            return self.name == other.upper()

        if isinstance(other, Gender):
            return self is other

        return False


@total_ordering
class WorkFlowStatus(Enum):
    OPEN = 1
    IN_PROGRESS = 2
    REVIEW = 3
    COMPLETE = 4

    def __lt__(self, other):
        if isinstance(other, int):
            return self.value < other

        if isinstance(other, WorkFlowStatus):
            return self.value < other.value

        return False


def main():
    for g in Gender:
        print(g)

    print(Gender.MALE == 1)
    print(Gender.MALE == "FEMALE")

    print(WorkFlowStatus.IN_PROGRESS < 2)
    print(WorkFlowStatus.IN_PROGRESS < WorkFlowStatus.COMPLETE)


if __name__ == '__main__':
    main()
