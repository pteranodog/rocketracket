from flask import Flask, request
from flask_socketio import SocketIO

app = Flask(__name__)
sio = SocketIO(app)
rooms = {}


class GameState:
    def __init__(self):
        pass


class Player:
    def __init__(self):
        self.status = 'connected'
        self.team = None

    def disconnect(self):
        self.status = 'disconnected'

    def reconnect(self):
        self.status = 'connected'


class Station:
    def __init__(self, uid):
        self.uid = uid
        self.code = '0000'


class Room:
    def __init__(self, room_number, rocket_uid):
        self.number = room_number
        self.stations = {'rocket': Station(rocket_uid), 'missioncontrol': None, 'crawler': None,
                         'fueltanks': None, 'launchtower': None, 'astronautcomplex': None}
        self.players = {}
        self.state = GameState()

    def add_player(self, player):
        self.players.update({player, Player()})

    def player_disconnected(self, player):
        self.players[player].disconnect()

    def player_reconnected(self, player):
        self.players[player].reconnect()

    def add_station(self, station_type, uid):
        self.stations.update({station_type, Station(uid)})

    def start(self):
        pass


@sio.on('connect')
def new_connection():
    pass


@sio.on('new rocket')
def new_rocket(room):
    rooms.update({room, Room(room, request.sid)})
