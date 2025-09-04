from email.header import make_header


class Car:
    wheels=4

    # Метод инициализации
    def __init__(self, make, model,year):
    # Атрибуты экземпляра
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    # Метод экземпляра
    def drive(self, distance):
        self.odometer += distance
        return f"Driving {distance} km. Total: {self.odometer} km"

    #Создание объекта
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.make) #Вывод: Toyota
print(my_car.drive(100)) #Вывод: Driving 100 km. Total: 100 km
