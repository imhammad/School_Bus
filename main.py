import tkinter as tk
from tkinter import messagebox, simpledialog


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

    def get_students_str(self):
        if not self.students:
            return "No students assigned yet."
        return "\n".join(f"{s.name} (Grade {s.grade})" for s in self.students)

# Class for managing the app

class SchoolBusAppGUI:

    def __init__(self, root):
        self.buses = []
        self.root = root
        self.root.title("School Bus System")
        self.root.geometry("500x400")

    



    
    # To run the menu loop

    def run(self):

        while True:

            print("---------- School Bus ----------")
            print("1. Add Bus")
            print("2. List Buses")
            print("3. Assign Students to Bus")
            print("4. View Students in Bus")
            print("5. Exit")

            choice = input("Enter Choice: ")

            if choice == '1':
                self.add_bus()

            elif choice == '2':
                self.list_buses()

            elif choice == '3':
                self.assign_student()

            elif choice == '4':
                self.view_bus_students()

            elif choice == '5':
                print("Thank You, and GoodBye!")

                break

            else:
                print("Invalid choice.")

# To Run the APP!

app = SchoolBusApp()

app.run()
        





        


        



            
