class Student:
    def __init__(self,name: str,age: int):
        self.name = name
        self.__age = age
    def set_age(self,age: int):
        if age < 0 or age >200:
            raise Exception(f"{age} is not valid.lry")
        self.__age= age
    def get_age(self):
        return self.__age

    age = property(fget = get_age,fset=set_age)
    def __str__(self):
        return f"{self.name},{self.__age}"

def main():
    student = Student("jack",18)
    student.age=-3
    student.set_age(3)
    print(student)

if __name__=="__main__":
    main()