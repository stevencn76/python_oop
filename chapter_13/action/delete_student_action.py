from chapter_13.action.action import Action


class DeleteStudentAction(Action):
    def execute(self):
        print("Delete a student")
