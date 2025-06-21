# 为什么需要枚举
#
# 如何定义枚举
# 枚举成员的name 和value
# 通过name和value访问成员
# 遍历枚举成员
# 枚举的继承
from enum import Enum
class Gender(Enum):
    MALE = 1
    FEMALE =2

class Student:
    def __init__(self,gender:Gender):
        self.gender = gender
def main():
    print(type(Gender.MALE))
    print(Gender.MALE.name)
    print(Gender.MALE.value)
    student = Student(Gender.MALE)
    if student.gender == Gender.MALE:
        print("this student is a male")
    else:
        print("the student is a female")

    s_gender = "MALE"
    # student.gender = Gender[s_gender]
    # print(student.gender.name)
    print(Gender[s_gender])
    i_gender = 2
    print(Gender(i_gender))



if __name__ == "__main__":
    main()