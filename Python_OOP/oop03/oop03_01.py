class Student:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def say_hello(self,msg):
        print(f'hello {self.name} ,我们在开会，{msg}')

def main():
    # 1.create a physical object
    # 2. call __init__() to initialize this object
    s1 = Student('lirongyao',32,'男')
    s1.say_hello('zhonggongyida')
    print(s1.name)
if __name__=='__main__':
    main()