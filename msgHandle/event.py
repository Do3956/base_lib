from eventManager import register, ClassEventManager


@register(ClassEventManager)
class Hero:
    def __init__(self, name):
        self.hp = 10
        self.name = name

    def fight(self, defender):
        print(f"{self.name} fight {defender.name}")

    def is_dead(self):
        return self.hp <= 0

    def hurt(self):
        self.add_hp(-2)

    def add_hp(self, _hp):
        self.hp += _hp


@register(ClassEventManager)
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
            t_fight = ClassEventManager().call_event(
                True, attacker, 'fight', defender)
            t_hurt = ClassEventManager().call_event(True, defender, 'hurt')
            attacker, defender = self.__swap(attacker, defender)
        print(f'winner is {defender.name}')


if __name__ == "__main__":
    f = FightBox(Hero(1), Hero(2))
    f.fight()
