class Car:
    color = None
    fuel = None
    brand = None
    model = None

    def go(self):
        print("Автомобиль едет")

    def turn(self):
        print("Автомобиль поворачивает")

    def stop(self):
        print("Автомобиль останавливается")

    def get_info(self):
        print(f"Автомобиль марки {self.brand}, модель {self.model}")
        print(f"Цвет: {self.color}")
        print(f"Количество топлива: {self.fuel}")

myCar = Car()
myCar.color = 'grey'
myCar.fuel = 65
myCar.brand = 'Audi'
myCar.model = 'A5'

myCar.go()
myCar.turn()
myCar.stop()
myCar.get_info()