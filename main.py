# Простая текстовая боевую игру, где игрок и компьютер управляют героями с различными характеристиками.
# Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу,
# пока у одного из героев не закончится здоровье.

import random
import math

# Класс Hero представляет героя в игре.

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20
        self.defense = 5  # Новая характеристика защиты
        

    def attack(self, target):

        chance = random.random()
        if chance < target.dodge_chance: #шанс уклониться
            print(f"{target.name} уклоняется от атаки {self.name}.")
            return
        elif chance <= 0.2: #шанс вылечиться
            self.use_special_ability(self)

        self.power_coefficient = random.uniform(0.8, 1.2)
        power = math.ceil(self.attack_power * self.power_coefficient - target.defense)

        if critical_hit:  # Увеличиваем урон в два раза для критического удара
            power *= 2
            print(f"Критический удар!")

        if power < 0:
            power = 0

        target.health -= power
        print(f"{self.name} атакует {target.name} и наносит {power} урона.")
        print(f'Здоровье {target.name}: {target.health}')

    def is_alive(self):
        return self.health > 0

    def is_alive(self):
        return self.health > 0

    def use_special_ability(self, target):  #Лечение героя
        # Пример способности: восстановление здоровья
        self.health += 20
        print(f"{self.name} использует способность восстановления здоровья! Он восстанавливает 20 здоровья.")


# Класс Game представляет игру.

class Game:
    def __init__(self, player: Hero, computer: Hero):
        self.hero = player
        self.monster = computer

    def start(self):
        while self.hero.is_alive() and self.monster.is_alive():
            self.hero.attack(self.monster)
            self.monster.attack(self.hero)
        if self.hero.is_alive():
            print(f"Победил {self.hero.name}!")
        else:
            print(f"Победил {self.monster.name}!")


# Инициализация игры
# Создание героев

player = Hero("Сергей")
computer = Hero("Монстр")

# Запуск игры

game = Game(player, computer)
game.start()
