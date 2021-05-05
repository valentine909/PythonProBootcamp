# In PyCharm change Settings->Editor->Color Scheme->Console Font->Line spacing->0.7 for better print_maze.
# 1. A robot '@' is randomly placed in the maze and faces one of the directions.
# 2. Robot should preferably go right from current position in order to escape the maze.
# 3. If going right is not possible then go straight or go left or turn left
# 4. The task is to write an algorithm which allows the robot to escape the given maze.
import time
maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 1
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # 2
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 2, 1],  # 3
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],  # 4
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],  # 5
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # 6
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
#           1     2     3     4     5     6


def print_maze(m):
    for i in m:
        for j in i:
            if j == 1:
                print('#', end='', sep='')
            elif j == 2:
                print('*', end='', sep='')
            elif j == 3:
                print('@', end='', sep='')
            else:
                print('.', end='', sep='')
        print()


class Robot:
    def __init__(self, x, y, face):
        self.x = x
        self.y = y
        self.face = face
        maze[x][y] = 3
        print_maze(maze)

    def move(self, dx, dy):
        maze[self.x][self.y] = 0  # left floor symbol behind
        maze[self.x + dx][self.y + dy] = 3  # set character symbol
        self.x += dx
        self.y += dy
        print_maze(maze)

    def check_surrounds(self, dx, dy):
        allowed = (0, 2, 3)
        if maze[self.x + dx][self.y + dy] in allowed:
            return True
        else:
            return False

    def actions_from_current_direction(self):
        # list of (dx, dy, new_direction) tuples corresponding to moving to the right,
        # straight or left, or turning left side
        actions = [[(0, 1, 1), (-1, 0, 0), (0, -1, 3), (0, 0, 3)],  # from facing north
                   [(1, 0, 2), (0, 1, 1), (-1, 0, 0), (0, 0, 0)],   # from facing east
                   [(0, -1, 3), (1, 0, 2), (0, 1, 1), (0, 0, 1)],   # from facing south
                   [(-1, 0, 0), (0, -1, 3), (1, 0, 2), (0, 0, 2)]   # from facing west
                   ]
        return actions[self.face]

    def set_face(self, new_face):
        self.face = new_face


def place_robot():
    import random
    # direction: 0 - north, 1 - east, 2 - south, 3 - west
    direction = random.randint(0, 3)
    while 1:
        x = random.randint(2, 12)
        y = random.randint(0, 10)
        if maze[x][y] == 0:
            return x, y, direction


def win_point():
    for i, row in enumerate(maze):
        for j, column in enumerate(row):
            if column == 2:
                return i, j


x, y, d = place_robot()
robot = Robot(x, y, d)
win = win_point()
while not (robot.x, robot.y) == win:
    time.sleep(0.5)
    for i in robot.actions_from_current_direction():
        if robot.check_surrounds(i[0], i[1]):
            robot.move(i[0], i[1])
            robot.set_face(i[2])
            break
