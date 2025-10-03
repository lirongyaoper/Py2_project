class UpperCase:
    def __init__(self,initial_value = None):
        self.value = initial_value #存储实际数据
    def __get__(self,instance,owner):
        return self.value.upper()# 读取时转为大写
    def __set__(self, instance, value):
        self.value= value

class Person:
    name = UpperCase("alice") #类属性由描述符进行管理


def main():
    p = Person()
    print(p.name)
    p.name = "bob"
    print(p.name)
if __name__=="__main__":
    main()