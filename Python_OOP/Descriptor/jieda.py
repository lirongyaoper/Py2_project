class IntegerField:
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('must be integer!')
        instance.__dict__[self.name] = value
        print(f'【self】: {str(self)}, 【intance】: {str(instance)}, 【instance.__dict__】: {instance.__dict__}, 【value】: {value}')
    def __set_name__(self, owner, name):
        self.name = name
        print(f'【owner】: {owner}, 【self.name】: {self.name}, 【name】：{name}')

class User:
    age = IntegerField()


def main():

    u = User()
    u.age = 20
    # u.age = '20'

if __name__ =="__main__":
    main()