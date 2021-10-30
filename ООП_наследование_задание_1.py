# импортируем функции из библиотеки math для рассчёта расстояния
from math import radians, sin, cos, acos
class Point:
    def __init__(self, latitude, longitude):
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)
    # считаем расстояние между двумя точками в км
    def distance(self, other):
        cos_d = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(other.latitude) * cos(
        self.longitude - other.longitude)
        return 6371 * acos(cos_d)

class City(Point):
    def __init__(self, latitude, longitude, name, population):
        # допишите код: сохраните свойства родителя
        super().__init__(latitude, longitude)
        # и добавьте свойства name и population
        self.name = name
        self.population = population
    def show(self):
        print(f"Город {self.name}, население {self.population} чел.")

class Mountain(Point):
    # допишите код: напишите конструктор, в нём сохраните свойства родителя и добавьте свойства name и height
    def __init__(self, latitude, longitude, name, height):
        super().__init__(latitude, longitude)
        self.name = name
        self.height = height
    # Переопределите метод show(self):
    # информацию о горе нужно вывести в формате:
    # "Высота горы <название> - <высота> м."
    def show(self):
        print(f"Высота горы {self.name} - {self.height} м.")


Check = Mountain(100,200,'Check',100)
Check.show()
