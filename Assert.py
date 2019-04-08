'''Исключение'''
def exc(text):
    assert text != ''
    print(str(text) + '!')

exc('asd')

def test(number):
    assert number > 0
    print(str(number))

test(10)
