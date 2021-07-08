import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []

    def create_car(self):
        if random.randrange(0, 100) / 100 > 0.8:
            self.car_list.append(Car())

    def move_cars(self):
        for car in self.car_list:
            if car.xcor() > -310:
                car.move()
            else:
                self.car_list.remove(car)

    def collision_with_car(self, player):
        for car in self.car_list:
            if player.distance(car) < 20:
                return True
        return False


class Car(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.color(random.choice(COLORS))
        self.pu()
        self.shapesize(stretch_wid=1, stretch_len=1.5)
        self.setheading(180)
        self.goto(295, random.randrange(-240, 261, 20))

    def move(self):
        self.forward(MOVE_INCREMENT)

