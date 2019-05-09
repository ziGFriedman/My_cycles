import json

def way_better(filename):
    print('reading file with way_better()')
    with open(filename) as f:
        return f.read()

if __name__ == '__main__':
    data = way_better('data.json')
    print('raw data is', data, type(data))
    print()

    # From string to object:
    obj = json.loads(data)     # из json в python словарь
    print(obj, type(obj))

    print(obj['object'], obj['boolean'])     # смотрим что лежит по ключу object и boolean
    print()

    # From object to string:
    print('dumping object to text:')
    obj['new-value'] = 'secret'
    print(json.dumps(obj, sort_keys = True, indent = 4))     # запись нового значения из python в текст вида json, sort_keys - форматирование кода, indent - отступ
    
