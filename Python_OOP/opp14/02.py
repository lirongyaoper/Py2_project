from enum import Enum

# 定义枚举类
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# 访问枚举成员
print(Color.RED)        # Color.RED
print(Color.RED.name)   # 'RED'
print(Color.RED.value)  # 1

# 比较枚举成员
assert Color.RED == Color.RED  # True
assert Color.RED is Color.RED  # True (单例特性)
assert Color.RED != Color.GREEN

# 禁止直接比较值 (需显式.value)
# print(Color.RED == 1)  # False (类型安全!)