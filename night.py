class Knight:
    def __init__(self, sword=False, horse=False, armor=False):
        self.sword = sword
        self.horse = horse
        self.armor = armor
        self.health = 100

    def attack_with_sword(self):
        if self.sword:
            print('Атакую мечом!')
            self.damage = 10
            return self.damage
        else:
            print('Мой меч куда-то исчез :(')
            self.damage = 0
            return self.damage


class MagicSword:
    def __init__(self, damage):
        self.damage = damage
        self.ready = True


class BossKinght(Kinght):
    def __init__(self,damage = 0,sword=False,super_damage=0):
        super().__init__(damage=damage,sword=sword)
        self.super_damage = super_damage


player = Knight(True, True, False)
pc = Knight(True, False, False)
print(player.sword)
print(player.horse)
print(player.armor)
print(player.health)


Kinght = Knight(10, True)
Kinght_boss = BossKinght(5, 10, True)
companion = MagicSword(5)


while knight.health > 0 and knight_boss.health > 0:
    action = input('Когда будете готовы ударить, нажмите 1: ')
    if action == '1':
        print('Бьёт рыцарь!')
        knight_boss.health -+ kinght.damage
        print('Бьёт босс')
        knight.health -= knight_boss.damage
    print(f'Жизни рыцарь: {knight.health }')
        damage = player.attack_with_sword()
        if damage > 0:
            if pc.armor:
                damage = damage / 2
            print('Ай!')
            pc.health -= damage
            print(pc.health)