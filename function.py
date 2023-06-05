path = "phone_book.txt"
def output_info(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            print(*line.split(';'), end='')

def input_info(file_name: str):
    with open(file_name, 'r+', encoding='utf-8') as data:
        record_id = 0
        for line in data:
            if line != '':
                record_id = line.split(';', 1)[0]
        print('Введите ФИО и телефон через пробел')
        line = f'{int(record_id) + 1};' + ';'.join(input().split()[:4]) + ';\n'
        confirm = confirmation('добавить ')
        if confirm == 'y':
            data.write(line)

def find_zadanie():
    print('Выберите цифру: ')
    print('0 - ID, 1 - фамилия, 2 - имя, 3 - отчество, 4 - телефон, 9 - выход')
    char = input()
    while char not in ('0', '1', '2', '3', '4', '9'):
        print('Данные не верны')
        print('Выберите цифру: ')
        print('0 - ID, 1 - фамилия, 2 - имя, 3 - отчество, 4 - телефон, 9 - выход')
        char = input()
    if char != '0':
        inp = input('введите необходимое значение\n')
        return char, inp
    else:
        return '9', '9'

def find_info(file_name: str, char, condition):
    if condition != '9':
        printed = False
        with open(file_name, 'r', encoding='utf-8') as data:
            for line in data:
                if condition == line.split(';')[int(char)]:
                    print(*line.split(';'))
                    printed = True
        if not printed:
            print("Ничего не найдено")
        return printed

def check_id_record(file_name: str, text: str):
    decision = input(f'Знаешь ID? {text}? 1 - да, 2 - нет, 9 - выход\n')
    while decision not in ('1', '9'):
        if decision != '2':
            print('Данные не верны')
        else:
            find_info(path, *find_zadanie())
        decision = input(f'Знаешь ID? {text}? 1 - да, 2 - нет, 9 - выход\n')
    if decision == '1':
        record_id = input('Введите ID, 9 - выход\n')
        while not find_info(file_name, '0', record_id) and record_id != '9':
            record_id = input('Введите ID, 9 - выход\n')
        return record_id
    return decision

def confirmation(text: str):
    confirm = input(f"Подтвердите {text} запись: y - yes, n - no\n")
    while confirm not in ('y', 'n'):
        print('Неверные данные')
        confirm = input(f"Подтвердите {text} запись: y - yes, n - no\n")
    return confirm

def replace_record_line(file_name: str, record_id, replaced_line: str):
    replaced = ''
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            replaced += line
            if record_id == line.split(';', 1)[0]:
                replaced = replaced.replace(line, replaced_line)
    with open(file_name, 'w', encoding='utf-8') as data:
        data.write(replaced)

def change_records(file_name: str):
    record_id = check_id_record(file_name, 'изменения')
    if record_id != '9':
        replaced_line = f'{int(record_id)};' + ';'.join(
            input('Введите ФИО и телефон через пробел\n').split()[:4]) + ';\n'
        confirm = confirmation('изменение')
        if confirm == 'y':
            replace_record_line(file_name, record_id, replaced_line)

def delete_records(file_name: str):
    record_id = check_id_record(file_name, 'удаление')
    if record_id != '9':
        confirm = confirmation('изменение')
        if confirm == 'y':
            replace_record_line(file_name, record_id, '')