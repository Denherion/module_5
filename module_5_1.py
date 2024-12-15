# Задача "Developer - не только разработчик"

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floor = 0 # устанавливаем стартовое значение этажа
        # если заданное значение для нового этажа ..., то...
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else: # усли условия соблюдаются, тогда
            for floor in range(new_floor):
                floor += 1
                print(int(floor))


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)