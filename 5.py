class RoomObject:
    def __init__(self, name: str, coordinates: list[float]):
        self.name = name
        self.coordinates = coordinates

    def set_coordinates(self, new_coordinates: list[float]):
        self.coordinates = new_coordinates

    def __repr__(self):
        return f"{self.name}(координати={self.coordinates})"


class Bed(RoomObject):
    def __init__(self, coordinates: list[float]):
        super().__init__("Bed", coordinates)


class Table(RoomObject):
    def __init__(self, coordinates: list[float]):
        super().__init__("Table", coordinates)


class Carpet(RoomObject):
    def __init__(self, coordinates: list[float]):
        super().__init__("Carpet", coordinates)


class TV(RoomObject):
    def __init__(self, coordinates: list[float]):
        super().__init__("TV", coordinates)


class Room:
    def __init__(self, name: str):
        self.name = name
        self.objects: list[RoomObject] = []

    def add_object(self, obj: RoomObject):
        self.objects.append(obj)
        print(f" Додано об'єкт: {obj.name}")

    def remove_object(self, obj_name: str):
        for obj in self.objects:
            if obj.name.lower() == obj_name.lower():
                self.objects.remove(obj)
                print(f" Видалено об'єкт: {obj.name}")
                return True
        print(f" Об'єкт '{obj_name}' не знайдено в кімнаті.")
        return False

    def rearrangement(self, obj_name: str, new_coordinates: list[float]):
        for obj in self.objects:
            if obj.name.lower() == obj_name.lower():
                old_coords = obj.coordinates
                obj.set_coordinates(new_coordinates)
                print(f" Переставлено {obj.name}: {old_coords} -> {new_coordinates}")
                return True
        print(f" Перестановку не виконано: об'єкт '{obj_name}' не знайдено.")
        return False

    def show_room(self):
        print(f"\n---  Кімната мрії: {self.name} ---")
        if not self.objects:
            print("Кімната порожня.")
        else:
            for obj in self.objects:
                print(f"  • {obj}")
        print("-" * 35 + "\n")


if __name__ == "__main__":
    my_dream_room = Room("Затишна спальня")

    bed = Bed([0, 0])
    table = Table([5, 2])
    carpet = Carpet([2, 2])
    tv = TV([5, 5])

    my_dream_room.add_object(bed)
    my_dream_room.add_object(table)
    my_dream_room.add_object(carpet)
    my_dream_room.add_object(tv)

    for obj in my_dream_room.objects:
        print(f'Предмет:{obj.name}')

    my_dream_room.show_room()

    my_dream_room.rearrangement("Bed", [1, 1])
    my_dream_room.rearrangement("Carpet", [1.5, 1.5])

    my_dream_room.remove_object("TV")

    my_dream_room.show_room()
