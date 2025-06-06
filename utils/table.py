class Seat:  # seat class
    def __init__(self):
        self.free = True  # At first,seats are empty
        self.occupant = None  # No people's name yet

    def set_occupant(
        self, name: str
    ) -> bool:  # name is a string. If seat is unoccupant, assign it to a person(name)
        if self.free == True:  # if the seat is empty
            self.occupant = name  # assign this seat to a name
            self.free = False  # change the seat state as occupied already
            return True  # assigned successfully
        else:
            False  # assign failed

    def remove_occupant(self) -> str:
        name = (
            self.occupant
        )  # the person who seated down here now but will goes to other seat after
        self.occupant = None  # the person left their previous seat
        self.free = True  # change the seat state as empty
        return name  # get the name of this person


class Table:
    def __init__(self, capacity: int, seats):
        self.capacity = capacity
        self.seats = [Seat() for i in range(capacity)]

    def has_free_spot(self):
        for seat in self.seats:  # check free seat one by one
            if seat.free == True:  # return bool if it's free
                return True
            else:
                False

    def assign_seat(self, name: str) -> bool:  # name is a string. If seat is not free,
        for seat in seats:  # check all seats
            if seat.free:
                seat.set.occupant(
                    name
                )  # using the set_occupant method of Class Seat to assign this empty seat to a name
                return True
        return False

    def left_capacity(self):
        return sum(
            1 for seat in self.seats if seat.free
        )  # plus 1 once there is a empty seat then get a sum
