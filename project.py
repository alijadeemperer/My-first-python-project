class Student:
    def __init__(self, name, math, science, english, urdu, history, geography):
        self.name = name
        self.math = int(math)
        self.science = int(science)
        self.english = int(english)
        self.urdu = int(urdu)
        self.history = int(history)
        self.geography = int(geography)
        self.total = self.math + self.science + self.english + self.urdu + self.history + self.geography
        self.average = self.total / 6
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.average >= 90:
            return "A+"
        elif self.average >= 80:
            return "A"
        elif self.average >= 70:
            return "B"
        elif self.average >= 60:
            return "C"
        elif self.average >= 50:
            return "D"
        else:
            return "F"

    def display_report(self):
        print(f"\nReport Card for {self.name}")
        print(f"Math = {self.math}")
        print(f"Science = {self.science}")
        print(f"English = {self.english}")
        print(f"Urdu = {self.urdu}")
        print(f"History = {self.history}")
        print(f"Geography = {self.geography}")
        print(f"Total = {self.total}")
        print(f"Average = {self.average:.2f}")
        print(f"Grade = {self.grade}")


students = []

def save_to_student_database():
    with open("student.csv", "w") as file:
        for student in students:
            file.write(f"{student.name},{student.math},{student.science},{student.english},{student.urdu},{student.history},{student.geography}\n")
    print("Student data saved to file.")

def add_student():
    name = input("Enter student name: ")
    try:
        math = int(input("Enter marks in Math: "))
        science = int(input("Enter marks in Science: "))
        english = int(input("Enter marks in English: "))
        urdu = int(input("Enter marks in Urdu: "))
        history = int(input("Enter marks in History: "))
        geography = int(input("Enter marks in Geography: "))
    except ValueError:
        print("Invalid input. Marks must be numbers.")
        return

    student = Student(name, math, science, english, urdu, history, geography)
    students.append(student)
    save_to_student_database()
    print("Student record added successfully.")

def load_from_file():
    try:
        students.clear()  # Remove old data before loading
        with open("student.csv", "r") as file:
            for line in file:
                name, math, science, english, urdu, history, geography = line.strip().split(",")
                student = Student(name, math, science, english, urdu, history, geography)
                students.append(student)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("File not found. Add some students first.")
    except Exception as e:
        print("Error loading data:", e)

def display_all_student():
    if not students:
        print("No student records found.")
    else:
        print(f"\nTotal Students: {len(students)}")
        for student in students:
            student.display_report()

def edit_student_database():
    if not students:
        print("No student data to edit. Load or add first.")
        return

    name = input("Enter the student name to edit: ")
    for student in students:
        if student.name.lower() == name.lower():
            try:
                student.math = int(input("Enter new Math marks: "))
                student.science = int(input("Enter new Science marks: "))
                student.english = int(input("Enter new English marks: "))
                student.urdu = int(input("Enter new Urdu marks: "))
                student.history = int(input("Enter new History marks: "))
                student.geography = int(input("Enter new Geography marks: "))
            except ValueError:
                print("Invalid input.")
                return

            student.total = student.math + student.science + student.english + student.urdu + student.history + student.geography
            student.average = student.total / 6
            student.grade = student.calculate_grade()
            save_to_student_database()
            print("Student record updated.")
            return

    print("Student not found.")

def main():
    load_from_file()  # Load data automatically at start

    while True:
        print("\n--- Student Database Menu ---")
        print("1. Add Student")
        print("2. Edit Student")
        print("3. Display All Students")
        print("4. Reload from File")
        print("5. Exit")
        choice = input("Please enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            edit_student_database()
        elif choice == "3":
            display_all_student()
        elif choice == "4":
            load_from_file()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

main()