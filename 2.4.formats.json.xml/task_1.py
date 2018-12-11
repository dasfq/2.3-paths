import json, codecs

def get_words_list():
    with codecs.open('files/newsafr.json', 'r', 'utf_8_sig') as f:
        news_data = json.load(f)
        words_list = []
        for i in news_data['rss']['channel']['items']:
            words_list.extend((filter(lambda x: len(x) > 6, i['description'].split())))
        return(words_list)


def get_frequent():
    words_list = get_words_list()
    words_dict = {}
    for i in words_list:
        words_dict[i] = words_list.count(i)
    top_10_list = sorted(words_dict.items(), key = lambda item:item[1], reverse=True)
    print(top_10_list[0:10])

get_frequent()

# def get_frequent():
#     words_list = get_words_list()
#     qty_list = []
#     top_10_dict = {}
#     words_dict = {}
#     for i in words_list:
#         words_dict[i] = words_list.count(i)
#     for a,b in words_dict.items():
#         qty_list.append(b)
#     for i in range(1, 10):
#         max_ind = qty_list.index(max(qty_list))
#         max_num = qty_list.pop(max_ind)
#         for a,b in words_dict.items():
#             if b == max_num:
#                 top_10_dict[a] = b
#     print(top_10_dict)


# 1) открыть файл
# 2) прочитать файл
# 3) отобрать слова длиннее 6сим в список:
#     - перебрать все новости:
#         -зайти в items;
#         - for i in items...
# 4) сделать счётчик для подсчёта сколько раз встречается элемент списка, складывая в словарь слово:число^
# 5) берём все количества в список
# 6) Цикл 10 раз:
#     6.1) попаем элемент(самый большой) в переменную max
#     6.2) Берём items из словаря, сравниваем значение с max, если true то берём ключ в список.
# 6) Выводим список ключей
