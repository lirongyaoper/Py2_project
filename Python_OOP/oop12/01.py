class Person:
    def __init__(self):
        self.name = 'jack'
    def say(self):
        print("Hello from Person")



class Student(Person):
    def __init__(self):
        super().__init__()
        self.school= 'Abc'
    def say(self):
        print("Hello from Student")


def main():
    student = Student()
    student.say()

    person= Person()
    person.say()



if __name__ == '__main__':
    main()