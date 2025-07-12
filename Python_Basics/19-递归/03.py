def nn(n):
    if n ==1:
        return 1
    return n*nn(n-1)
print(nn(100))