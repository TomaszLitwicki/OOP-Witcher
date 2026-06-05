import random


class Bone:
    def __init__(self, name):
        self.result = None
        self.name : str = name
        self.k = int(self.name.removeprefix('k'))

    def throw(self):
        self.result = random.randrange(self.k) + 1

        match self.result:
            case 1 :
                a = 'oczko'
            case x if x in range (2, 5) :
                a = 'oczka'
            case _ :
                a = 'oczek'

        print(f'Rzut kością {self.name} - wylosowano {self.result} {a}.')

class Witcher:
    def __init__(self, name, school, strength = 15, health = 100):
        self.name = name
        self.school = school
        self.strength = strength
        self.health = health
        self.dice = Bone('k10')


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
            print(f'Wiedźmin otrzymuje {damage} punktów obrażeń i zostaje mu {self.health} punktów życia')


    def drink_potion(self, amount):
        if self.health == 0:
            print('Nie możesz wskrzesić Wiedżmina tym eliksirem.')
        else:
            print(f'Wiedźmin wypija miksturę i przywraca {min(amount, 100 - self.health)} punktów życia')
            self.health = min (100, self.health + amount)


    def attack(self, monster):
        print(f'Wiedźmin atakuje potwora {monster.species}')
        self.dice.throw()
        monster.take_damage(self.strength + self.dice.result)


class Monster:
    def __init__(self, strength = 10, health = 50 ):
        self.species = self.__class__.__name__
        self.strength = strength
        self.health = health
        self.dice = Bone('k6')


    def strike(self, witcher):
        print(f'{self.species} atakuje {witcher.name}\'a')
        self.dice.throw()
        witcher.take_damage(self.strength + self.dice.result)


    def take_damage(self, damage):
        if self.health <= damage:
            self.health = 0
            print(f'Potwór otrzymuje {damage} punktów obrażeń i ginie.')
        else:
            self.health = self.health - damage
            print(f'Potwór otrzymuje {damage} punktów obrażeń i zostaje mu {self.health} punktów życia.')


class Utopiec(Monster):
    def __init__(self):
        super().__init__()

    def regenerate(self):
        if self.health > 0:
            self.health += 5
            print(f'{self.species} ukrywa się w wodzie i regeneruje 5 punktów życia.')

if __name__ == '__main__':
    geralt = Witcher('Geralt', 'Wilka')
    utopiec = Utopiec()
    geralt.describe()
    print()
    print('Gdzieś na wiedźmińskim szlaku Geralt napotyka na swojego pierwszego potwora... jest to UTOPIEC!')
    print()
    print('ZACZYNA SIĘ POJEDYNEK:')
    print()

    while geralt.health > 0 and utopiec.health > 0:
        utopiec.strike(geralt)
        geralt.attack(utopiec)
        utopiec.regenerate()
        print()

    if geralt.health > 0:
        print(f'Pojedynek wygrał Geralt i zostało mu {geralt.health} punktów życia')

        geralt.drink_potion(50)
        geralt.describe()

