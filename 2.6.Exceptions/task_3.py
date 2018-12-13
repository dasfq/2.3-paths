documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "nameE": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people(number):
    doc_number = input('Введите номер документа')
    for i in number:
        if i['number'] == doc_number:
            print(i['name'])
            return i['name']
    print('wrong document number')


def list(docs):
    for i in docs:
        print(i['type'], ' "', i['number'], '"', ' "', i['name'], '"', sep="")


def shelf(shelves):
    doc_number = input('Введите номер док-та')
    number = "number is not found"
    for i in shelves:
        if doc_number in shelves[i]:
            number = i
    print('Shelf number: {}'.format(number))


def add(doc_list, shelves_dict):
    keys = []
    for key in doc_list[1].keys():
        keys.append(key)
    values = input(
        'Введите:  тип, номер док-та, имя владельца и номер полки, на котором он будет храниться через запятую БЕЗ ПРОБЕЛОВ.').split(
        ',')
    new_doc = {keys[0]: values[0], keys[1]: values[1], keys[2]: values[2], }
    doc_list.append(new_doc)

    shelf_number = values[3]
    if shelf_number in shelves_dict:
        shelf_content = shelves_dict[shelf_number]
        shelf_content.append(values[1])
        shelves_dict[shelf_number] = shelf_content
    else:
        shelves_dict[shelf_number] = [values[1]]

    print(shelves_dict)
    print(doc_list)


def choose_command():
    command = input('Введите команду (p/l/s/a/n)\n')
    if command == 'p':
        people(documents)
    elif command == 'l':
        list(documents)
    elif command == 's':
        shelf(directories)
    elif command == 'a':
        add(documents, directories)
    elif command == 'n':
        print_names(documents)

#
#  ДОМАШНЕЕ ЗАДАНИЕ - ДОБАВЛЕННАЯ ФУНКЦИЯ, ВЫЗЫВЕТСЯ БУКВОЙ n:
#

def print_names(docs):
    for i in docs:
        try:
            print(i['name'])
        except KeyError:
            print("У документа отсутствует поле 'name'")



choose_command()
