def summary(n:int):
    if n  ==1:
        return 1
    return n+summary(n-1)

count = summary(500)
print(count)