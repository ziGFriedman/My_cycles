'''Модуль, описывающий структуру данных - стек
# >>>clear()
# >>>is_empty()
# True
# >>>push(1)
# >>>push(2)
# >>>push(3)
# >>>is_empty()
# False
# >>>pop()
# 3
# >>>pop()
# 2
# >>>pop()
# 1
# >>>is_empty()
# True
'''

# Checking_the_correctness_bracket_sequence.py

_stack = []

def push(x):
    '''Добавляет элемент х в коней сека'''
    _stack.append(x)

def pop():
    x = _stack.pop()
    return x

def clear():
    _stack.clear()

def is_empty():
    return len(_stack) == 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()    # testmod(verbose=True) - показывает тест
