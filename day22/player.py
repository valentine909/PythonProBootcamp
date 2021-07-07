from score import Scoreboard
from paddle import Paddle


class Player:
    def __init__(self, name='first'):
        """
        :param scoreboard:
        :param paddle:
        :param name: Can be 'first' or 'second'
        """
        self.score = Scoreboard(player=name)
        self.paddle = Paddle(player=name)
