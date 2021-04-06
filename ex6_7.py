from random import randint
from question_6_7_add import add_data
from question_6_7_read import custom_read
from question_6_7_edit import edit


def add():
    """Аналог работы файла question_6_7_add - добавляет данные в файл bakery.csv"""
    if len(commands) == 1:
        print('Вы не ввели данные')
        while True:
            n = input('Сколько строк данных сгенерировать?\n>>> ')
            if n.isdigit():
                n = int(n)
                break
        for _ in range(n):
            add_data(str(randint(100, 10 ** 6) / 100))
    else:
        add_data(commands[1])
    print('Добавление данных выполнено')

def read():
    """Аналог работы файла question_6_7_read - читает файл bakery.csv в рамках указанных строк"""
    if len(commands) == 1 or not commands[1].isdigit():
        final = custom_read()
    elif len(commands) == 2 or not commands[2].isdigit():
        final = custom_read(int(commands[1]))
    else:
        final = custom_read(int(commands[1]), int(commands[2]))
    print(final)

def edb():
    """Аналог работы файла question_6_7_edit - заменяет указанную строку на указанное содержимое"""
    if len(commands) > 2 and commands[1].isdigit() and int(commands[1]):
        result = edit(int(commands[1]), commands[2])
    else:
        result = 'Введены неверные аргументы'
    print(result)


commands_dict = {'add': add, 'read': read, 'edit': edb}

action = input('Введите необходимую операцию со списком. Для справки ничего не вводите, нажмите Enter\n>>> ')

commands = action.split()
if not commands or not commands_dict.get(commands[0]):
    print('HELP\n'
          'add <data> - для добавления <data> в файл\n'
          'read <start> <stop> - чтение файла начиная со строки <start> до строки <stop>.\n'
          '                      по умолчанию начало и конец файла.\n'
          'edit <num> <data> - записывает <data> заменяя данные в строке номер <num>')
else:
    commands_dict.get(commands[0])()