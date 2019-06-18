'''
"((()))()((()))" - корректно
"())(()" - некорректно"
"[(())]([])" - корректно
"[), [(])" - некорректно
'''
# Для очередной скобки:
# Если она открывающаяся, то запоминая ее в стек;
# Если она закрывающаяся:
# Стек пуст
import A_stack

def is_braces_sequence_correct():
    '''
    Проверяет корректность скобочной послед-ти из круглых и квадратных скобок

    >>> is_braces_sequence_correct("(([()]))[]")
    True
    >>> is_braces_sequence_correct("([()]))")
    False
    >>> is_braces_sequence_correct("(([])[]")
    False
    >>> is_braces_sequence_correct("](([()]))[]")
    False
    '''
    for brace in s:
        if brace not in "()[]":
            continue
        if brace in "(["



if __name__ == '__main__':
    import doctest
    doctest.testmod()
