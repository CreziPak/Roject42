class Dog:
    def __init__(self, name: str, age: int, breed: str):
        """

        :param name: Кличка
        :param age: Возраст
        :param breed: Порода собаки
        """
        self.name = name
        self.age = age
        self.breed = breed
        print(f"{self.name} создан")

    def sit(self):
        """Дать команду сидеть"""
        print(f"{self.name.title()} элегантно сел")

    def jump(self):
        """Дать команду жёстко прыгнуть"""
        print(f"{self.name.title()} сделал жёсткий прыжок")

    def bark(self):
        """Дать команду голос"""
        print(f"{self.name.title()} мирно полаял")

god_ym = Dog("Нига", 4, "Дворняга")
god_ym.sit()
god_ym.jump()
god_ym.bark()


print(god_ym.age)
print(god_ym.breed)

god_ym1 = Dog("Чёрн", 7, "Волкобой")
god_ym1.sit()
god_ym1.jump()
god_ym1.bark()


print(god_ym1.age)
print(god_ym1.breed)





