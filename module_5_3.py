class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self,new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
                print("Такого этажа не существует")
        else:
            for floor in range(new_floor):
                    print(floor + 1)

    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f"Название:{self.name}, кол-во этажей:{self.number_of_floors}"

    def __eq__(self,other):
        isinstance(other, int)
        return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other.number_of_floors, int):
           return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)






h1 = House("Жк Шишкин лес", 17)
h2 = House("ЖК Пупкино", 97)
h1.go_to(7)
h2.go_to(100)
print(len(h1))
print(len(h2))
print(h2)
print(h1)
print(h2 == h1)
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)
h1 = h1 + 80
print(h1)
print(h1 == h2)
h1 += 80
print(h1)
h2 = h2 + 80
print(h2)

