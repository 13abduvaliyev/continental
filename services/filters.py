from models.room import Room


def filter_rooms(rooms: Room, size: int, price: float) -> Room:
    return [room for room in rooms if room.size == size or room.price <= price]