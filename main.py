
class Student:
    def __init__(self, name, grade):

        self.name = name
        self.grade = grade

class Bus:
    def __init__(self, number, driver):

        self.number = number
        self.driver = driver
        self.students = []

        # To Add Students to the bus

        def add_student(self, student):

            self.students.append(student)
        
        # To Show the current Students in the bus

        def show_students(self):

            if not self.students:
                print("No students assigned yet.")
            else:
                for s in self.students:
                    print(f"{s.name} (Grade {s.grade})")

    # Class for managing the app

class SchoolBusApp:

    def __init__(self):
        
        self.buses = []

    # To add a new bus
        
    def add_bus(self):

        number = input("Enter bus number: ")
        driver = input("Enter driver name: ")

        self.buses.append(Bus(number, driver))
        print("Bus Added!")


    # To list all the buses

    def list_buses(self):

        if not self.buses:
            print("No buses available.")
        else:
            for i, b in enumerate(self.buses):
                print(f"{i+1}. Bus {b.number} - Driver: {b.driver}")
        
