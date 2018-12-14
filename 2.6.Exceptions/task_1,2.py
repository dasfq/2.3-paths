def calc():
    input_data = input('Введите знак операции и два положительных числа через пробелы: \n')
    data_list = []
    for i in input_data.split(' '):
        try:
            data_list.append(int(i))
        except ValueError:
            data_list.append(i)
    # print(data_list)
    for i in data_list:
        try:
            assert i >= 0
        except TypeError:
            pass
        except AssertionError:
            print("Введите положительные числа")
            raise SystemExit
    try:
        if data_list[0] == "+":
            result = data_list[1] + data_list[2]
            print(result)
        elif data_list[0] == "-":
            result = data_list[1] - data_list[2]
            print(result)
        elif data_list[0] == "*":
            result = data_list[1] * data_list[2]
            print(result)
        elif data_list[0] == "/":
            result = data_list[1] / data_list[2]
            print(result)
        else:
            print("Введите корректный знак арифметической операции")
    except TypeError:
        print('Введите корректные данные')
        raise SystemExit

calc()