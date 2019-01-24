countries = {
    'Thailand': {'country_sea': True, 'country_schengen': False, 'exchange_rate': 2, 'temperature': 28,
                 'living_cost': 900},
    'Germany': {'country_sea': True, 'country_schengen': True, 'exchange_rate': 74, 'temperature': 10,
                'living_cost': 50},
    'Poland': {'country_sea': True, 'country_schengen': True, 'exchange_rate': 18, 'temperature': 8,
               'living_cost': 150},
    'Russia': {'country_sea': True, 'country_schengen': False, 'exchange_rate': 1, 'temperature': 5,
               'living_cost': 2000}
}

budget = 20000

countries['Turkie'] = {
    'country_sea': True, 'country_schengen': True, 'exchange_rate': 2, 'temperature': 30, 'living_cost': 300
}
countries['Italy'] = {
    'country_sea': True, 'country_schengen': True, 'exchange_rate': 3, 'temperature': 30, 'living_cost': 500
}
countries['Czech'] = {
    'country_sea': False, 'country_schengen': True, 'exchange_rate': 2, 'temperature': 20, 'living_cost': 400
}
print(countries, '\n')

cntry_list_1 = []
for country in countries:
    params = countries[country]
    # print(params,'\n')

    if (params['country_schengen'] and (params['living_cost'] * 7) <= budget) or (
            (params['living_cost'] * 10) <= budget and params['country_sea'] and params['temperature'] > 20):
        cntry_list_1.append(country)
print(
    'Список стран, где хватит бюджета на неделю проживания И находятся в Шенгенской зоне ИЛИ (хватит бюджета на 10 дней проживания И есть выход к морю И средняя температура больше 20): {} \n'.format(
        cntry_list_1))

cook_book = {
    'салат':
        [
            ['картофель', 100],
            ['морковь ', 50],
            ['огурцы', 50],
            ['горошек', 30],
            ['майонез', 70],
        ],
    'пицца':
        [
            ['сыр', 50],
            ['томаты', 50],
            ['тесто', 100],
            ['бекон', 30],
            ['колбаса', 30],
        ],
    'фруктовый десерт':
        [
            ['хурма', 60],
            ['киви', 60],
            ['творог', 60],
            ['сахар', 10],
            ['мед', 50],
        ]
}

person = 3

for dish_name in cook_book:
    ing_list = cook_book[dish_name]
    buy_list = []
    for ing_qty in ing_list:
        buy_list.append([ing_qty[0], ing_qty[1] * person])
    print('Для приготовления', dish_name, 'на', person, 'человек требуется:', buy_list, '\n')
