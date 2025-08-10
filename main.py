
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

        
        