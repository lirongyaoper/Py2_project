# 数据描述符（实现 __set__）
class DataDescriptor:
    def __get__(self, instance, owner):
        print("调用 DataDescriptor 的 __get__")
        #print(f'self: {self}, instance: {instance}, owner: {owner}')  #返回 self: <__main__.DataDescriptor object at 0x0000016A9DF33140>, instance: <__main__.MyClass object at 0x0000016A9DF33260>, owner: <class '__main__.MyClass'>
        return "来自数据描述符的值"

    def __set__(self, instance, value):
        print("调用 DataDescriptor 的 __set__")
        instance.__dict__["attr"] = value  # 绕过描述符，直接存储到实例字典

# 非数据描述符（仅实现 __get__）
class NonDataDescriptor:
    def __get__(self, instance, owner):
        print("调用 NonDataDescriptor 的 __get__")
        return "来自非数据描述符的值"


class MyClass:
    attr = DataDescriptor()  # 数据描述符（优先级最高）
    lazy_attr = NonDataDescriptor()  # 非数据描述符（优先级最低）

def main():
    obj = MyClass()
    #场景一 ： 数据描述符 vs 实例属性
    obj.attr = '直接设置的实例属性值'
    print('obj.__dict__=',obj.__dict__)
    print('obj.attr=', obj.attr)
    obj.lazy_attr = '直接设置的实例属性值'
    print(f'obj.lazy_attr=', obj.lazy_attr)
    del obj.lazy_attr
    print("obj.lazy_attr = ",obj.lazy_attr)

if __name__=="__main__":
    main()