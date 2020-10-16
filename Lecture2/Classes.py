# class Point():
#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2

# p = Point(5, 2)

# print(p.x)
# print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3) 
names = ["Harry", "Draco", "Hermione", "Ginny"]

for name in names:
    success = flight.add_passenger(name)

    if success:
        print(f"{name} was added to passengers list.")
    else:
        print(f"{name} can't fly.")
