import random

turn = [" на лево", " на право"]


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} автомобиль начал движение'

    def stop(self):
        return f'{self.name} автомобиль остановился'

    def turn(self):
        return f'{self.name} автомобиль повернул {random.choice(turn)}'

    def show_speed(self):
        return f'Текущая скорость: {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Вы превышаете срокость на {self.speed - 60} км/час'
        else:
            return f'Текущая скорость автомобиля {self.name}: {self.speed}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Вы превышаете срокость на {self.speed - 40} км/час'
        else:
            return f'Текущая скорость автомобиля {self.name}: {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if self.is_police == True:
            print("Полиция")


town_car = TownCar(65, 'red', 'Lada', False)
print(f'{town_car.name} {town_car.show_speed()}\n')

work_car = WorkCar(50, 'yellow', 'Honda', False)
print(f'{work_car.name} {work_car.show_speed()}\n')

sport_car = SportCar(100, 'blue', 'mitsubishi', False)
print(f'{sport_car.name} {sport_car.show_speed()}\n')

police = PoliceCar(80, 'black', 'lamborghini', True)
print(f'{police.name} {police.show_speed()}')
