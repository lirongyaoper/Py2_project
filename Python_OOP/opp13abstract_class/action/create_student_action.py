from Python_OOP.opp13abstract_class.action.action import Action

class CreateStudentAction(Action):
    def execute(self):
        print("Create a new student")