def print_sequence(n:int):
    print(n)
    next_num = n -1
    if next_num >0:
        print_sequence(next_num)

print_sequence(100)