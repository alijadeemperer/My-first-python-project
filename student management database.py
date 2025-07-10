class Student:
    def __init__(self, name,math,science,english,urdu,history,geography):
        self.name      = name
        self.math      = math
        self.science   = science
        self.english   = english
        self.urdu      = urdu
        self.history   = history
        self.geography = geography
        self.total     = self.math + self.science + self.english + self.urdu + self.history + self.geography
        self.average   = self.total/6
        self.grade     = self.calculate_grade()
        
    def calculate_grade(self):
        if self.average >= 90:
            return "A+"
        elif self.average >= 80:
            return ("A")
        elif self.average >= 70:
            return("B")
        elif self.average >= 60:
            return("C")
        elif self.average >= 50:
            return("D")
        else:
             return("F")
    
    def display_report(self):
        print(f" Report card for {self.name}")
        print(f" MATH = {self.math}")
        print(f" Science = {self.science}")
        print(f" English = {self.english}")
        print(f" Urdu = {self.urdu}")
        print(f" History =  {self.history}")
        print(f" Geography = {self.geography}")
        print(f" total = {self.total}")
        print(f" average = {self.average}")
        print(f"grade = {self.grade}")
    
students = []

def save_to_student_database():
    with open("student.csv","w") as file:
        for student in students:
            file.write(f"{student.name},{student.math},{student.science},{student.english},{student.urdu},{student.history},{student.geography},{student.total},{student.average},{student.grade}\n")
              
def add_student():
    name = input("Enter student name:")
    try:
        math       = int(input("Enter student marks in math:"))
        science    = int(input("Enter student marks in science:"))
        english    = int(input("Enter student marks in english:"))
        urdu       = int(input("Enter student marks in urdu:"))
        history    = int(input("Enter student marks in history:"))
        geography  = int(input("Enter student marks in geography:"))
    except ValueError:
        print("Value must be in number")
    
    student = Student(name,math,science,english,urdu,history,geography)
    students.append(student)
    save_to_student_database()
    print("The student record is added to the file")
    return

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
      print("student not found")
    else:
         print(f"the student name are {len(students)}")
         for student in students:
             student.display_report()
             
              
def edit_student_database():
    if not students:
        print("record not added yet")
        return
      
    name = input("enter the student name\n")
    for student in students:
        if student.name.lower() == name.lower():
            try:
                math       = int(input("Enter student marks in math:\n"))
                science    = int(input("Enter student marks in science:\n"))
                english    = int(input("Enter student marks in english:\n"))
                urdu       = int(input("Enter student marks in urdu:\n"))
                history    = int(input("Enter student marks in history:\n"))
                geography  = int(input("Enter student marks in geography:\n"))
            except:
                print("invalid input")
                return
            student.math      = math
            student.science   = science
            student.english   = english
            student.urdu      = urdu 
            student.history   = history
            student.geography = geography
            student.total     = student.math+student.science+student.english+student.urdu+student.history+student.geography
            student.average   = student.total / 6
            student.grade     = student.calculate_grade()
            save_to_student_database()
            print("The student record isd added successfully\n")
            return

def main():
    load_from_file() 
    while True:
           print("welcome to the student database")
           print("1.add student")
           print("2.edit student")
           print("3.display all ")  
           print("4.load from file")
           print("5.exist")
           choice = input("please enter your choice:\n")
           
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
               print("invalid choice")

main()
