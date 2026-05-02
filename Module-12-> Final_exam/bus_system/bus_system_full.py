class Bus:
    def __init__(self,number,route,total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0
        self.seat_plan = []

        current_row = []
        for i in range(total_seats):
            row_char = chr(65 + (i//4))
            seat_no = (i%4) +1
            current_row.append(f"{row_char}{seat_no}")

            if len(current_row) == 4 or i == total_seats -1:
                self.seat_plan.append(current_row)
                current_row = []
    
    def show_seat_plan(self):
        print(f"Seat plan for bus no : {self.number} Route : {self.route} seat : {self.total_seats}")
        for row in self.seat_plan:
            for i,seat in enumerate(row):
                print(f"{seat}",end=" ")
                if i == 1:
                    print(" ",end="\t")
            print()
        print(f"  Avialable: {self.available_seats()}  Booked: {self.booked_seats}\n")

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self):
        if self.available_seats() > 0:
            for r in self.seat_plan:
                for i,s in enumerate(r):
                    if s != "X":
                        r[i] = "X"
                        self.booked_seats += 1
        else:
            print("No seat available.")

class Passenger:
    def __init__(self,name,phone,bus):
        self.name = name 
        self.phone = phone
        self.bus = bus

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

class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"
 
    def login(self,username,password):
        if self.username == username and self.password == password:
            return True
        return False

system = BusSystem()
admin = Admin()

while True:
    print("*-----------User Menu--------------*")
    print("1. Admin Login")
    print("2. Book Ticket")
    print("3. View Buses")
    print("4. Exit")
    print("*-------------------------------*")
    choice = int(input("Enter your Choice : "))

    if choice == 1:
        username = input("Username: ")
        password = input("Password: ")
        if admin.login(username,password) == True :
            print("Login Sucessfull!")
            while True:
                print("*-------------------------------*")
                print("ADMIN MENU")
                print("1. Add Bus")
                print("2. View All Buses")
                print("3. Logout")
                print("*-------------------------------*")
                admin_choice = int(input("Enter your choice: "))
                if admin_choice == 1:
                    bus_number = input("Bus Number: ")
                    route = input("Route: ")
                    seats = int(input("Total Seats: "))
                    system.add_bus(bus_number,route,seats,)
                elif admin_choice == 2:
                    # system.show_buses()
                    for bus in system.buses:
                        bus.show_seat_plan()
                elif admin_choice == 3:
                    print("Logged out.")
                    break
                else:
                    print("Invalid choice.")
        else:
            print("Wrong username or password.")
    
    elif choice == 2:
        system.show_buses()
        if system.buses:
            bus_num = input("Enter bus number: ")
            for bus in system.buses:
                if bus.number == bus_num:
                    bus.show_seat_plan()
            name = input("Your name: ")
            phone = input("Phone No: ")
            ticket_count = int(input("Enter how many ticket you want : "))
            booking_seats = []
            for i in range(ticket_count):
                booking_seats.append(input("Enter your seat no : "))
            system.book_ticket(bus_num,name,phone,booking_seats)
    
    elif choice == 3:
        system.show_buses()
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid option try again.")