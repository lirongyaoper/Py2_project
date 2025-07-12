def times(n):
    return lambda x:x*n

double = times(2)
print(double(3))