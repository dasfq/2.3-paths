class Animal():
    name = ""
    hunger = 100
    weight = 0
    color = ""
    voice = ""
    total_weight = []
    animals_list = []

    def feed_all():
        for i in Animal.animals_list:
            i.hunger -= 25

    def feed(self):
        self.hunger -= 25

    def call(self):
        print(self.voice)

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.total_weight.append(self.weight)
        self.animals_list.append(self)


class Milkable():
    milk = 100

    def get_milk(self):
        self.milk -= 25


class Eggable():
    eggs = 5

    def get_eggs(self):
        self.eggs -= 1


class Fleecable():
    fleece = 100

    def get_fleece(self):
        self.fleece -= 25


class Goose(Animal, Eggable):
    voice = "goose_voice"


class Chicken(Animal, Eggable):
    voice = "Co-co-co"


class Duck(Animal, Eggable):
    voice = "Crya-crya-crya"


class Cow(Milkable, Animal):
    voice = "Mooo-oo-o"


class Goat(Milkable, Animal):
    voice = "Beeee-ee-e"


class Sheep(Milkable, Animal, Fleecable):
    voice = "Meee-ee-e"


goose_1 = Goose('Серый', 5)
goose_1.get_eggs()
goose_2 = Goose('Белый', 4)

cow_1 = Cow('Манька', 200)
cow_1.call()
cow_1.get_milk()
print(cow_1.milk)

sheep_1 = Sheep('Кудрявый', 50)
sheep_2 = Sheep('Барашек', 60)
sheep_1.call()

chicken_1 = Chicken('Ко-ко', 3)
chicken_2 = Chicken('Кукареку', 4)

goat_1 = Goat('Рога', 60)
goat_2 = Goat('Копыта', 70)
goat_1.call()

duck_1 = Duck('Кряква', 4)
print(duck_1.name)



print('Вес экземпляров:', Animal.total_weight)
print('Общий вес:', sum(duck_1.total_weight))
max_weight = max(Animal.total_weight)

for i in range(len(Animal.animals_list)):
    if Animal.animals_list[i].weight >= max_weight:
        max_weight = Animal.animals_list[i].weight
        max_weight_name = Animal.animals_list[i].name

print('Максимальный вес: {}'.format(max_weight))
print('Животное с максимальным весом:{}'.format(max_weight_name))

Animal.feed_all()
print("Голод: {}%".format(cow_1.hunger))