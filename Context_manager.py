'''Чтение файлов'''
def read_file(filename):
    print('reading file with read_file()')
    try:
        f = open(filename)
        content = f.read()
        f.close()
    finally:
        print('Finale')
    return content

# с использованием контекмтного менеджера (файл будет закрыт сам, после конкретных действий)
def way_better(filename):
    print('reading file with way_better()')
    with open(filename) as f:
        return f.read()

'''Перезапись в файл'''
def write_to_file(filename, content, mode = 'w'):     # если mode = 'a' - идёт добавление в конец файла
    with open(filename, mode = mode) as f:
        f.write(content)
