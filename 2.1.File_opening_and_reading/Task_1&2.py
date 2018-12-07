def Make_cook_book():
  cook_book = {}
  with open('recepies.txt') as f:
    for line in f:
        name = line.rstrip()
        qty = int(f.readline())
        ingr_list = []
        i = 1
        while i <= qty:
            ingr_dict = {}
            ingr = [a.strip() for a in f.readline().split('|')]
            ingr_dict['ingredient_name'] = ingr[0]
            ingr_dict['quantity'] = int(ingr[1])
            ingr_dict['measure'] = ingr[2]
            ingr_list.append(ingr_dict)
            i += 1
        cook_book[name] = ingr_list
        f.readline()
    print(cook_book)
    return(cook_book)


def get_shop_list_by_dishes():
    book = Make_cook_book()
    ingredients_dict = {}
    dishes_list = list(input('Введите названия блюд через запятую без пробелов: \n').split(','))
    print(dishes_list)
    person_num = int(input('Введите количество человек: \n'))
    for dish, ingredients_list in book.items():
        if dish in dishes_list:
            for ing in ingredients_list:
                qty_dict = {}
                qty_dict['measure'] = ing['measure']
                qty_dict['quantity'] = int(ing['quantity']) * person_num
                ingredients_dict[ing['ingredient_name']] = qty_dict
        else:
            print('Таких блюд нет в книге рецептов')
    print(ingredients_dict)

get_shop_list_by_dishes()
