from logging import StreamHandler


class Score:
    def __init__(self,default = 0):
        self.__score = default
    def __set__(self,instance,value):
        if not isinstance(value,int):
            raise TypeError("Score must be integer")
        if not 0<= value <=100:
            raise ValueError("Valid value must be in [0,100]")
        self.__score = value
    def __get__ (self,instance,owner):
        return self.__score
    def __delete__(self):
        del self.__score

class Student:
    math = Score(0)
    chinese = Score(0)
    english = Score(0)
    def __init__(self,name,math,chinese,english):
        self.name = name
        self.math = math
        self.chinese = chinese
        self.english = english
    def __repr__(self):
        return "<Student: {},math:{},chinese:{},english:{}>".format(self.name,self.math,self.chinese,self.english)
def main():
    stu1 = Student("小明",76,"120",68)
    print(stu1)

if __name__ =="__main__":
    main()