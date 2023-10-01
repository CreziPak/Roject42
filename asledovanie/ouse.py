import time
class House:
    """Дом"""
    def __init__(self, area: float, rooms: int, address: str):
        """

        :param area: Площадь дома
        :param rooms: Количество комнат
        :param adress: Адрес
        """
        self.area = area
        self.rooms = rooms
        self.address = address
        self.door_closed = True

    def open_door(self):
        """Открыть дверь"""
        if self.door_closed != False:
            self.door_closed = False
            print(f'Дверь дома по адресу {self.address} открыта, брат')
        else:
            print('Дверь уже открыта, гений')

    def closed_door(self):
        """Закрыть дверь"""
        if self.door_closed != True:
            self.door_closed = True
            print(f'Дверь дома по адресу {self.address} закрыта брат')
        else:
            print('Дверь уже закрыта, гений')


class MultiStoryHouse(House):
    '''Многоэтажный дом'''
    def __init__(self, area: float, rooms: int, address: str, floors: int, has_elevator = bool):
        """

        :param area: Площадь дома
        :param rooms: Количество комнат
        :param adress: Адрес
        :param floors: Количество этажей
        """
        super().__init__(area, rooms, address)
        self.floors = floors
        self.has_elevator = has_elevator #Имеется ли лифт
        self.elevator_floor = 1 #Этаж, на котором стоит лифт

    def call_elevator(self, floor: int):
        """Вызвать лифт
        :param floor: Этаж назначения
        """
        floor_time = 3 #Время прохождения лифтом одного этажа
        floors = abs(floor - self.elevator_floor) #Количество проденных этажей
        total_time = floors * floor_time
        print(f'Лифт отправляется с этажа {sself.elevator_floor} на этаж {floor}')
        time.sleep(total_time)
        print('Лифт приехал')
        self.elevator_floor = floor





esuoh_ym = House(80, 3, 'г. Ливер, ул. Имени первой буквы')
print(f'Количество комнат в доме по адресу {esuoh_ym.address}: {esuoh_ym.rooms}')
print(f'У дома {esuoh_ym.address} площадь: {esuoh_ym.area}')
esuoh_ym.open_door()
esuoh_ym.open_door()
esuoh_ym.closed_door()
esuoh_ym.closed_door()
