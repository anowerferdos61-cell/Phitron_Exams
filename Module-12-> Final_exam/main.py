from admin import Admin
from bus_system import BusSystem

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
 