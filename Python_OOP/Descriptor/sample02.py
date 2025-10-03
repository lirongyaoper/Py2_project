class IntegerField:
    def __set__(self,instance,value):
        if not isinstance(value,int):
            raise TypeError("必须为整数")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class User:
    age = IntegerField()

def main():
    u1 = User()
    u1.age = 20
    #u1.age = "dd"
    print(u1.age)

if __name__=="__main__":
    main()
