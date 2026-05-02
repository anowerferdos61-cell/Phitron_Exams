from buses import Bus
from pasenger import Passenger

class BusSystem:
    def __init__(self):
        self.buses = []
        self.passenger = []
    
    def add_bus(self,number,route,seats):
        bus = Bus(number,route,seats)
        self.buses.append(bus)
        print(f"Bus number {number} added on route {route}")
    
    def show_buses(self):
        if not self.buses:
            print("There is no Bus")
        else:
            print("-----BUS LIST-----")
            for bus in self.buses:
                print(f"Bus no : {bus.number}\tRoute : {bus.route}\tAvailavle seat : {bus.available_seats()}/{bus.total_seats}")
                # bus.show_seat_plan()
    
    def book_ticket(self,bus_num,name,phone,booking_seat):  
        bus = None
        for b in self.buses:
            if b.number == bus_num:
                bus = b
                break
        if bus is None:
            print("There is no bus.\n")
            return
        
        booked_tickets = []
        for seat in booking_seat:
            seat = seat.strip().upper()
            r = ord(seat[0]) - 65
            c = int(seat[1]) - 1

            if r < 0 or r >= len(bus.seat_plan) or c < 0 or c >= len(bus.seat_plan[r]):
                print(f"{seat} does not exist.")
                continue

            if bus.seat_plan[r][c] == "X":
                print(f"{seat} is already booked.")
            else:
                bus.seat_plan[r][c] = "X"
                bus.booked_seats += 1
                booked_tickets.append(seat)

        if booked_tickets:
            passenger = Passenger(name, phone, bus)
            self.passenger.append(passenger)
            print('*----------------------------------------*')
            print("Ticket Booked Successfully.")
            print('*----------------------------------------*')
            print(f"Name : {name}\tPhone : {phone}\tBus : {bus_num}")
            print("Your tickets : ",end=" ")
            for i in booked_tickets:
                print(i,end=" ")
            print(f"\nPrice : {500*len(booked_tickets)} TK")
            # bus.show_seat_plan()