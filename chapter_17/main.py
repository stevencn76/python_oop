class Parent1:
    def __init__(self):
        pass

    def render(self):
        print("parent 1")

    def hello(self):
        print("hello parent 1")


class Parent2:
    def __init__(self):
        pass

    def render(self):
        print("parent 2")

    def hello(self):
        print("hello parent 2")


class Child(Parent2, Parent1):
    def __init__(self):
        Parent1.__init__(self)

    def render(self):
        super().render()

    def hello(self):
        Parent1.hello(self)


def main():
    child = Child()
    child.render()
    child.hello()


if __name__ == '__main__':
    main()
