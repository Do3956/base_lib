# from eventManager import ClassManager
from threadPool import thread_pool


# @ClassManager.register
class Hero:
    def __init__(self, name):
        self.hp = 10
        self.name = name

    def fight(self, person):
        print(f'{self.name} fight {person.name}')

    def is_dead(self):
        return self.hp <= 0

    def hurt(self):
        self.add_hp(-2)

    def add_hp(self, _hp):
        self.hp += _hp

# @ClassManager.register
class FightBox:
    def __init__(self, leftHero, rightHero):
        self.leftHero = leftHero
        self.rightHero = rightHero

    def __swap(self, left, right):
        return right, left

    def __fish(self):
        return self.leftHero.is_dead() or self.rightHero.is_dead()

    def fight(self):
        attacker = self.leftHero
        defender = self.rightHero
        while not self.__fish():
            t_fight = thread_pool.workers.submit(attacker.fight, defender)
            t_fight.result()
            t_hurt = thread_pool.workers.submit(defender.hurt)
            t_hurt.result()
            attacker, defender = self.__swap(attacker, defender)
        print(f'winner is {defender.name}')

if __name__ == "__main__":
    f = FightBox(Hero(1), Hero(2))
    f.fight()
