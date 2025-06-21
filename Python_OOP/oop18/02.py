class Student:
    def __init__(self,name,math,chinese,english):
        self.name = name
        self.math = math
        self.chinese = chinese
        self.english = english
    @property
    def math(self):
        return self.__math
    @math.setter
    def math(self,value):
        if 0<=value <=100:
            self.__math = value
        else:
            raise ValueError("Valid value must be in[0,100]")
    @property
    def chinese(self):
        return self.__chinese
    @chinese.setter
    def chinese(self,value):
        if 0<= value <=100:
            self.__chinese = value
        else:
            raise ValueError("Valid value muse be in [0,100]")

    @property
    def english(self):
        return self.__english

    @english.setter
    def english(self, value):
        if 0 <= value <= 100:
            self.__english = value
        else:
            raise ValueError("Valid value muse be in [0,100]")
    def __repr__(self):
        return "<Student: {}, math:{}, chinese: {}, english:{}>".format(
                self.name, self.math, self.chinese, self.english
            )

def main():
    std1 = Student("liming",98,98,12)
    print(std1)

if __name__ == "__main__":
    main()