def upper(func):
    def inner(x,y):
        print('Result:', x, '+', y)
        result = func(x,y)
        return result
    return inner

@upper
def sum(x,y):
    print('---')
    return x+y

print(sum(2, 2))
