class Person:
    def __init__(self):
        print("Persion:inint is called")
        self.name = 'jack'

class Student(Person):
    def __init__(self):
        super().__init__()
        print("Student:init is called")
        self.school= 'Abc'


def main():
    student = Student()
    print(student.name)
    print(student.school)
    print(isinstance(student,Student))
    print(isinstance(student,Person))


if __name__ == '__main__':
    main()