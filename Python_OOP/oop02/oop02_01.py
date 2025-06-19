class Student:
    student_count = 10
def main():
    print(Student.__name__)
    print(Student.student_count)
    print(getattr(Student,"student_count"))
    print(getattr(Student,"unkonw","None"))
    Student.student_count=109
    print(Student.student_count)
    setattr(Student,"student_count",200)
    print(Student.student_count)

if __name__ == '__main__':
    main()