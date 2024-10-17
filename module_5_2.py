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

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название:{self.name}, кол-во этажей:{self.number_of_floors}"



h1 = House("Жк Шишкин лес", 17)
h2 = House("ЖК Пупкино", 97)
h1.go_to(7)
h2.go_to(100)
print(len(h1))
print(len(h2))
print(h2)
print(h1)