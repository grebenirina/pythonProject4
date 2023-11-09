class Airline:
    def __init__(self, destination, flight_number, aircraft_type, departure_time, weekdays):
        self.destination = destination
        self.flight_number = flight_number
        self.aircraft_type = aircraft_type
        self.departure_time = departure_time
        self.weekdays = weekdays

    def display_info(self):
        print("Destination: ", self.destination)
        print("Flight number: ", self.flight_number)
        print("Aircraft type: ", self.aircraft_type)
        print("Departure time: ", self.departure_time)
        print("Weekdays: ", self.weekdays)
        print("------------------------")


flights = [
    Airline("New York", "AW234", "Aeroflot 23", "10:20", ["Monday", "Friday"]),
    Airline("Paris", "BQ667", "Airfast 89", "18:56", ["Sunday", "Friday"]),
    Airline("London", "BA789", "Boeing 777", "09:15", ["Tuesday", "Saturday"]),
    Airline("Tokyo", "JL987", "Boeing 787", "17:10", ["Thursday", "Sunday"])
]
destination = "Paris"
print("Flights to ", destination)
for flight in flights:
    if flight.destination == destination:
        flight.display_info()
weekday = "Sunday"
print("Flights on ", weekday)
for flight in flights:
    if weekday in flight.weekdays:
        flight.display_info()
