#assignment - 3
#software engineering
class Flight:
    def __init__(self, flight_id, from_city, to_city, price):
        self.flight_id = flight_id
        self.from_city = from_city
        self.to_city = to_city
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights_by_city(self, city):
        city_flights = [flight for flight in self.flights if city in (flight.from_city, flight.to_city)]
        return city_flights

def main():
    flight_table = FlightTable()

    flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

    while True:
        print("MANASVI PRIYA    E.NO-E22CSEU1168     BATCH-39")
        print("\nHere are your Search Options:")
        print("1. Flights for a particular City")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            city = input("Enter the city code (e.g. BLR, BOM, BBI, HYD, JLR): ")
            city_flights = flight_table.search_flights_by_city(city)
            if city_flights:
                print("\nFlights for", city)
                for flight in city_flights:
                    print("Flight ID:", flight.flight_id)
                    print("From:", flight.from_city)
                    print("To:", flight.to_city)
                    print("Price:", flight.price)
            else:
                print("No flights found for", city)
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Please select a valid option. Your choice is Invalid")

if __name__ == "__main__":
    main()
