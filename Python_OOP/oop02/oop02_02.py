from pprint import pprint


class Student:
    student_count = 10
    student_address= 'chinese'
def main():
    print(Student.__name__)

    pprint(Student.__dict__)
if __name__ == '__main__':
    main()