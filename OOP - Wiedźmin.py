class Witcher:
    def __init__(self, name, school, health = 100):
        self.name = name
        self.school = school
        self.health = health


    def describe(self):
        if self.health > 20:
            print (f'Jestem {self.name} ze szkoły {self.school}. Mam {self.health} punktów życia')
        elif self.health > 0:
            print (f'Jestem {self.name} ze szkoły {self.school}. Mam tylko {self.health} punktów życia i jestem ranny!')
        else:
            print(f'Wiedźmin ma {self.health} punktów życia i jest martwy...')


    def take_damage(self, damage):
        if self.health <= damage:
            self.health = 0
            print('Wiedźmin ginie.')
        else:
            self.health = self.health - damage
            print(f'Wiedźmin otrzymuje {damage} punktów obrażeń.')


    def drink_potion(self, amount):
        if self.health == 0:
            print('Nie możesz wskrzesić Wiedżmina tym eliksirem.')
        else:
            print(f'Wiedźmin wypija miksturę i przywraca {min(amount, 100 - self.health)} punktów życia')
            self.health = min (100, self.health + amount)


    def attack(self, monster):
        print(f'Wiedźmin atakuje potwora {monster.species}')
        print(f'{monster.species} został pokonany. Chwała Wiedźminowi!!!')


class Monster:
    def __init__(self, species, strength):
        self.species = species
        self.strength = strength


    def strike(self, witcher):
        print(f'{self.species} atakuje {witcher.name}\'a')
        witcher.take_damage(self.strength)


geralt = Witcher('Geralt', 'Wilka')
gryf = Monster('Gryf', 40)
geralt.describe()
gryf.strike(geralt)
geralt.describe()
geralt.attack(gryf)
geralt.drink_potion(50)
geralt.describe()