
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self,new_floor):
        floor = 0
        if new_floor < 1 or new_floor > self.number_of_floors:
                print("Такого этажа не существует")
        else:
            for floor in range(new_floor):
                    print(floor + 1)
        return 0




h1 = House("Жк шишкин лес", 17)
h2 = House("ЖК Пупкино", 99)
h1.go_to(7)
h2.go_to(100)