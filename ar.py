class Vehicle:
    def __init__(self, color, power):
        self.color = color
        self.power = power

    def move_forward(self):
        print(f'Транспорт едет вперёд с мощностью {self.power}')

    def move_backward(self):
        print(f'Транспорт едет назад с мощностью {self.power}')


airplane_1 = Vehicle('желтый', 50)
car_2 = Vehicle('синий', 30)
print(airplane_1.color)
print(car_2.power)
airplane_1.move_forward()
car_2.move_forward()


class Bike(Vehicle):
    def __init__(self, color, power, pram):
        super().__init__(color, power)
        self.has_pram = pram

    def put_bandwagon(self):
        print('Подножка выставлена')


yamaha = Bike('Синий', 60, False)
print(yamaha.color)
print(f'Моитоцикл имеет коляску? {yamaha.has_pram }')
yamaha.put_bandwagon()
yamaha.move_forward()


class Car(Vehicle):
    def __init__(self, color, power, pram):
        super().__init__(color, power)
        self.has_pram = pram

    def zip_belt(self):
        print('Все ремни пристёгнуты')


Audi = Car('Белая', 60, False)
print(Audi.color)
print(f'Все двери закрыты? {Audi.has_pram}')
Audi.zip_belt()
Audi.move_forward()


while True:
    action = imput('когда будите готовы ударить нажмите 1;')
    if action == '1':
        damage = player.attack_with_sword()
        if damage > 0:
            if pc.armor:
                damage /= 2
    print() ('Ай')
    pc.health -= damage
    print(pc.health )