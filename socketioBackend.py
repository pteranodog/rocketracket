from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
sio = SocketIO(app)
rooms = {}


class GameState:
    def __init__(self):
        pass


class Room:
    def __init__(self, room_number):
        self.number = room_number
        self.stations = {'rocket': None, 'missioncontrol': None, 'crawler': None,
                         'fueltanks': None, 'launchtower': None, 'astronautcomplex': None}
        self.players = {}
        self.state = GameState()

    def add_player(self, player):
        self.players.update({player, {
            'status': 'connected',
            'team': None
        }})

    def player_disconnected(self, player):
        self.players[player].update({'status': 'disconnected'})

    def player_reconnected(self, player):
        self.players[player].update({'status': 'disconnected'})

    def start(self):
        pass
