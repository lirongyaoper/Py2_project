from Python_OOP.opp13abstract_class.action.action import Action
from Python_OOP.opp13abstract_class.action.create_student_action import CreateStudentAction
def execute_action(action:Action):
    action.execute()

def main():
    create_student_action = CreateStudentAction()
    execute_action(create_student_action)

if __name__=='__main__':
    main()

