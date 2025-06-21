class Person:
    color = 1
    def __init__(self):
        self.name = 'jack'
    def say(self):
        print("Hello from Person")

    def print_color(self):
        print(self.color)

class Student(Person):
    color = 2
    def __init__(self):
        super().__init__()
        self.school= 'Abc'
    def say(self):
        super().say()
        print("Hello from Student")
class Worker(Person):
    pass
def render(person: Person):
    person.say()

def main():
    student = Student()
    student.say()

    person= Person()
    person.say()
    worker1 = Worker()
    render(student)
    render( worker1)

    print(Student.color)
    student.print_color()



if __name__ == '__main__':
    main()