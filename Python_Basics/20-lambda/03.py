def get_full_name(first_name,last_name,formatter):
    return formatter(first_name,last_name)

def first_last(first_name,last_name):
    return f'{first_name}{last_name}'

def last_first(first_name, last_name):
    return f'{last_name}{first_name}'

print(get_full_name('jack','li',last_first))

# lambda 表达式写法
print(get_full_name('jack','li',lambda first_name,last_name:f'{last_name}{first_name}'))
print(get_full_name('jack','li',lambda first_name,last_name:f'{first_name}{last_name}'))