# task 1.
class StudentDatabase:
    student_list = []
    def add_student(self, student):
        self.student_list.append(student)


# task 2 and 9 also.
class Student:
    def __init__(self,student_id,name,department,is_enrolled,database):
        self.__student_id = student_id # private data.
        self._name = name #protected data
        self._department = department # protected data
        self.__is_enrolled = is_enrolled # private data 
        
        database.add_student(self)


    # task 4
    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print(f"student {self._name} is now enrolled.")
        else:
            print(f"student {self._name} is already enrolled.") # task 8


    # task 5.
    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f"student {self._name} has been dropped.")
        else:
            print(f"student {self._name} is not enrolled.") # task 8


    # task 6.
    def view_student_info(self):
        print(f"Student ID: {self.__student_id}, Name: {self._name}, Department: {self._department}, Enrolled: {self.__is_enrolled}")

    def get_student_id(self):
        return self.__student_id

DataBase =StudentDatabase()

#task 3.
s1 = Student(101,"Anower Ferdos","Department of Chemistry",True,DataBase)
s2 =Student(102,"Fahad Hossain","Department of IDMV",False,DataBase)
s3 = Student(103,"RUbel Ali","Department of Chemistry",False,DataBase)

while True:
    # task 7.
    print("----Student Management Menu----")
    print("1. view all students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")
    choice= input("Enter your choice (1-4): ")
    if choice == '1':
        for student in DataBase.student_list:
            student.view_student_info()
    elif choice =='2':
        student_id = input("Enter Student ID to enroll : ")
        for student in DataBase.student_list:
            if student_id == str(student.get_student_id()):
                student.enroll_student()
                break
        else:
            print("Invalid Student ID. student not found.") #task 8.

    elif choice == '3':
        student_id = input("Enter Student ID to drop: ")
        for student in DataBase.student_list:
            if student_id == str(student.get_student_id()):
                student.drop_student()
                break
        else:
            print("Invalid Student ID. student not found") #task 8
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")