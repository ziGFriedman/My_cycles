'''Пример написания декоратора'''
def decorator(func):
    func.counter = 1

    def fake(value):
        print('Runs:', func.counter)
        func.counter += 1
        return func(value)

    return fake    # Если функция возвращает функцию, то это декоратор

@decorator    # связь с декоратором (my_str = decorator(my_str))
def my_str(value):
    return str(value)

print(my_str(123))
print(my_str([]))
print(my_str({}))


'''Выводит время выполнения функции'''
import timeit

def decorator2(func):

    def fake(value):
        start_time = timeit.default_timer()
        result = func(value)
        print('Time is:', timeit.default_timer() - start_time)
        return result

    return fake

@decorator2
def my_str2(value):
    return str(value)

print(my_str2(123))
print(my_str2([]))
print(my_str2({}))
