from time import sleep


class TrafficLight:
    color = ('red', 'yellow', 'green')

    def running(self):
        x = 0
        while True:
            print(self.color[x])
            if x == 0:
                sleep(5)
            elif x == 1:
                sleep(2)
            elif x == 2:
                sleep(5)
            x += 1
            if x == 3:
                x = 0


traffic_light = TrafficLight()
traffic_light.running()

###############################################################################################

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate(self):
        result = self._length * self._width * 25 * 5 / 1000
        print(result)


road_calc = Road(20, 5000)
road_calc.calculate()

###################################################################################################

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return self._income_wage + self._income_bonus


pos = Position('Ivan', 'Ivanov', 'senior', {"wage": 150000, "bonus": 50000})
print(pos.get_full_name())
print(pos.get_total_income())

############################################################################################

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self. color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn_direction(self, direction):
        if direction == 'right':
            return 'Машина повернула направо'
        elif direction == 'left':
            return 'Машина повернула налево'

    def show_speed(self):
        return self.speed

    def show_everything(self):
        return self.name, self.show_speed(), self.color


class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            return f'{self.speed} км/ч. Скорость превышена!'


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            return f'{self.speed} км/ч. Скорость превышена!'


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


car = WorkCar(90, 'red', 'bmw', False)
print(car.show_everything())
print(car.go())
print(car.turn_direction('left'))
print(car.show_speed())

####################################################################################################

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationary):
    def draw(self):
        return "Рисунок ручкой"


class Pencil(Stationary):
    def draw(self):
        return "Рисунок карандашом"


class Handle(Stationary):
    def draw(self):
        return "Рисунок маркером"

some_shit = Stationary('Шит')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

print(some_shit.title)
print(some_shit.draw())
print(pen.title)
print(pen.draw())
