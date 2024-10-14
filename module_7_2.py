def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, "w", encoding='utf-8')
    counter = 1
    for item in strings:
        some_tuple = (counter, file.tell())
        strings_positions[some_tuple] = item
        file.write(item + '\n')
        counter += 1
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)



