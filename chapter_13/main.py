from chapter_13.action.action import Action
from chapter_13.action.create_student_action import CreateStudentAction
from chapter_13.action.delete_student_action import DeleteStudentAction


def execute_action(action: Action):
    action.execute()


def main():
    create_student_action = CreateStudentAction()
    delete_student_action = DeleteStudentAction()

    execute_action(create_student_action)
    # execute_action(delete_student_action)


if __name__ == '__main__':
    main()
