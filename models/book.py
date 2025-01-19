from .user import User
from .room import Room

class Book:
    def __init__(self, user: User, room: Room, empty_space):
        self.user = user
        self.room = room
        self.space = empty_space
    