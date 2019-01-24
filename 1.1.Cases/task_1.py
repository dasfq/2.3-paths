print('Введите курс евро:')
eur_rate = int(input())

print('Введите ваш бюджет в РУБ:')
budget = int(input())

print('Введите цену за номер в EUR:')
room_price_eur = int(input())

print('Введите кол-во дней:')
days_num = int(input())

print('Введите количество перелётов:')
flights_number = int(input())
flights_per_trip = 2

print('Введите цену перелёта в EUR:')
flight_price_eur = int(input())
flight_cost = flights_number * flights_per_trip * flight_price_eur

# meal cost
bfst_price_eur = 5 * eur_rate
print('Введите цену обеда в EUR:')
lunch_price_eur = int(input()) * eur_rate
meal_cost_eur = lunch_price_eur * days_num

# acoomodation cost
print('Завтрак включён в цену номера? (введите "y" или "n")')
a = str(input())
if a == 'n':
  room_price_eur += bfst_price_eur
  print('добавлено', bfst_price_eur, 'EUR к стоимости номера')
acc_cost = room_price_eur * days_num

total_cost_eur = meal_cost_eur + flight_cost + acc_cost

print('Стоимость перелёта:', flight_cost * eur_rate, 'руб.')
print('Стоимость проживания:',acc_cost * eur_rate,'РУБ.' )
print('Стоимость питания:',meal_cost_eur * eur_rate,'РУБ.')
print("Ваши расходы на путешествие",total_cost_eur,"EUR или",total_cost_eur * eur_rate,'РУБ')

if total_cost_eur * eur_rate > budget:
  print('Вы превысите свой бюджет')
else:
  print('Вы уложитесь в свой бюджет')