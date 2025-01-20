# Простая текстовая боевую игру, где игрок и компьютер управляют героями с различными характеристиками.
# Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу,
# пока у одного из героев не закончится здоровье.

import random
import math

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, target):
        self.power_coefficient = random.uniform(0.8, 1.2) # Добавлен коэффициент урона, для случайности урона
        power = math.ceil(self.attack_power * self.power_coefficient)
        target.health -= power
        print(f"{self.name} атакует {target.name} и наносит {power} урона.")
        print(f'Здоровье {target.name}: {target.health}')

    def is_alive(self):
        return self.health > 0

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

player = Hero("Сергей")
computer = Hero("Монстр")

game = Game(player, computer)
game.start()
