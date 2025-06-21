#抽象类
from abc import ABC, abstractmethod


# 1. 抽象类是一个不能被实例化的类
class Action(ABC):
    @abstractmethod
    def execute(self):
        pass


# 2. 抽象方法是一个没有具体实现的方法

# 3. 一个抽象类可以有或者没有抽象方法

# 4. python并没有直接支持抽象类，但是提供了一个模块来允许定义抽象类
