from turtle import Turtle


class Segment(Turtle):
    def __init__(self):
        super().__init__()
        self.segment = Turtle(shape='square', visible=False)
        self.segment.color('white')
        self.segment.pu()
        self.segment.showturtle()

    def move_to_position(self, other):
        x = other.get_position()
        self.segment.goto(x)

    def move(self):
        self.segment.forward(20)

    def set_position(self, x, y):
        self.segment.goto(x, y)

    def get_position(self):
        return self.segment.position()

    def turn_left(self):
        curr = self.segment.heading()
        self.segment.setheading(curr + 90)

    def turn_right(self):
        curr = self.segment.heading()
        self.segment.setheading(curr - 90)


class Snake:
    def __init__(self):
        self.snake = []
        self.head = None
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            seg = Segment()
            seg.set_position(0 - i * 20, 0)
            self.snake.append(seg)
        self.head = self.snake[0]

    def __len__(self):
        return len(self.snake)

    def tail_move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].move_to_position(self.snake[i - 1])

    def move_forward(self):
        self.tail_move()
        self.head.move()

    def to_the_left(self):
        self.head.turn_left()

    def to_the_right(self):
        self.head.turn_right()

