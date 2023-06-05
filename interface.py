def start ():
    path = 'phone_book.txt'

    try:
        file = open(path, 'r')
    except IOError:
        print('Создана новая телефонная книга -> phone_book.txt ')
        file = open(path, 'w')
    finally:
        file.close()