class Coords:
    def __init__(self, json):
        self.x = json.get('x')
        self.y = json.get('y')


class Snake:
    def __init__(self, json):
        self.id = json.get('id')
        self.name = json.get('name')
        self.health = json.get('health')

        if type(json.get('body')) == list:
            self.body = [Coords(x) for x in json['body']]

    def head(self):
        if getattr(self, 'body'):
            return self.body[0]


class Board:
    def __init__(self, json):
        self.height = json.get('height')
        self.width = json.get('width')

        if type(json.get('food')) == list:
            self.food = [Coords(x) for x in json['food']]

        if type(json.get('snakes')) == list:
            self.snakes = [Snake(x) for x in json['snakes']]


class Game:
    def __init__(self, json):
        self.id = json.get('id')


class SnakeRequest:
    def __init__(self, json):
        self.turn = json.get('turn')

        if type(json.get('game')) == dict:
            self.game = Game(json['game'])

        if type(json.get('board')) == dict:
            self.board = Board(json['board'])

        if type(json.get('you')) == dict:
            self.you = Snake(json['you'])


class MoveResponse(dict):
    def __init__(self, move):
        super().__init__()

        assert move in ['up', 'down', 'left', 'right'], \
            "Move must be one of [up, down, left, right]"
        self["move"] = move


class StartResponse(dict):
    def __init__(self, color):
        super().__init__()

        assert type(color) is str, "Color value must be string"
        self["color"] = color
