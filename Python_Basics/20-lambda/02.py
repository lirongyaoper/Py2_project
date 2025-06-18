def display(name,greeting):
    result = greeting(name)
    print(result)


display('mary',lambda name:f'Hello {name}')