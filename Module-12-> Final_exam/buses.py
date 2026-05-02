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