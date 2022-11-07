from chapter_13.action.action import Action


class CreateStudentAction(Action):
    def execute(self):
        print("Create a new student")
