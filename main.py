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

        # Background color (Can insert an image too here! hehe)
        self.root.config(bg="#ffeb99")

        tk.Label(root, text="School Bus Menu", font=("Arial", 20, "bold"), bg="#ffeb99").pack(pady=20)

        tk.Button(root, text="Add Bus", width=20, command=self.add_bus).pack(pady=5)
        tk.Button(root, text="List Buses", width=20, command=self.list_buses).pack(pady=5)
        tk.Button(root, text="Assign Student to Bus", width=20, command=self.assign_student).pack(pady=5)
        tk.Button(root, text="View Students in Bus", width=20, command=self.view_bus_students).pack(pady=5)
        tk.Button(root, text="Exit", width=20, command=root.quit).pack(pady=20)

    def add_bus(self):
        number = simpledialog.askstring("Bus Number", "Enter bus number:")
        driver = simpledialog.askstring("Driver Name", "Enter driver name:")
        if number and driver:
            self.buses.append(Bus(number, driver))
            messagebox.showinfo("Success", "Bus added!")


    



    
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
        





        


        



            
