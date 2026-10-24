
class Flight:
    def __init__(self, code, source, destination, seats, fare):
        self.code = code
        self.source = source
        self.destination = destination
        self.seats = seats
        self.fare = fare

    def show_flight(self):
        print(self.code, self.source, "to", self.destination,
              "| Seats:", self.seats, "| Fare:", self.fare)


class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def discount(self):
        return 0


class Student(Passenger):
    def discount(self):
        return 10


class Booking:
    def __init__(self, flight, passenger, tickets):
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets

    def show_booking(self):
        subtotal = self.flight.fare * self.tickets
        discount = subtotal * self.passenger.discount() / 100
        total = subtotal - discount

        print("\nBooking Confirmed!")
        print("Booking ID: BK1001")
        print("Passenger:", self.passenger.name)
        print("Age:", self.passenger.age)
        print("Flight:", self.flight.code)
        print("Route:", self.flight.source, "to", self.flight.destination)
        print("Tickets:", self.tickets)
        print("Subtotal: Rs.", subtotal)
        print("Discount: Rs.", discount)
        print("Final Amount: Rs.", total)


class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Mumbai", "Bengaluru", 15, 3500),
            Flight("PN303", "Pune", "Hyderabad", 25, 2500)
        ]
        self.booking = None

    def run(self):
        while True:
            print("\n1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                for flight in self.flights:
                    flight.show_flight()

            elif choice == "2":
                code = input("Enter flight code: ").upper()
                selected = None

                for flight in self.flights:
                    if flight.code == code:
                        selected = flight

                if selected is None:
                    print("Invalid flight code")
                    continue

                name = input("Enter passenger name: ").strip()

                try:
                    age = int(input("Enter age: "))
                    passenger_type = input(
                        "Passenger type (Regular/Student): "
                    ).strip().lower()
                    tickets = int(input("Enter number of tickets: "))
                except ValueError:
                    print("Please enter valid numbers")
                    continue

                if name == "" or age <= 0 or tickets <= 0:
                    print("Invalid passenger details")
                    continue

                if passenger_type not in ["regular", "student"]:
                    print("Invalid passenger type")
                    continue

                if tickets > selected.seats:
                    print("Not enough seats available")
                    continue

                if passenger_type == "student":
                    passenger = Student(name, age)
                else:
                    passenger = Passenger(name, age)

                self.booking = Booking(selected, passenger, tickets)
                selected.seats -= tickets
                self.booking.show_booking()

            elif choice == "3":
                if self.booking is None:
                    print("No booking found")
                else:
                    self.booking.show_booking()

            elif choice == "4":
                print("Thank you for using Kiran Air!")
                break

            else:
                print("Invalid choice")


app = FlightBookingSystem()
app.run()
