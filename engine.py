from function import *
from interface import start

path = "phone_book.txt"
start()

actions = {"1": "чтение телефонной книги",
           "2": "запись нового абонента",
           "3": "поиск абонента в книге",
           "4": "изменение абонента",
           "5": "удаление абонента",
           "9": "выход"}
action = None

while action != "9":
    print("Что вы хотите сделать?", *[f"{i} - {actions[i]}" for i in actions])
    action = input()
    while action not in actions:
        print("Что вы хотите сделать?", *[f"{i} - {actions[i]}" for i in actions])
        action = input()
        if action not in actions:
            print("Неверные данные")
    if action != "0":
        if action == "1":
            output_info(path)
        elif action == "2":
            input_info(path)
        elif action == "3":
            find_info(path, *find_info())
        elif action == "4":
            change_records(path)
        elif action == "5":
            delete_records(path)