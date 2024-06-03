import tkinter as tk
import pickle

class StudentRecord:
    def __init__(self):
        self.roll_number = 0
        self.name = ""
        self.physics_score = 0
        self.chemistry_score = 0
        self.maths_score = 0
        self.computer_score = 0
        self.english_score = 0
        self.total_score = 0
        self.percentage = 0
        self.grade = ""

    def add_record(self, roll, name, physics, chemistry, maths, computer, english):
        self.roll_number = int(roll)
        self.name = name.upper()
        self.physics_score = float(physics)
        self.chemistry_score = float(chemistry)
        self.maths_score = float(maths)
        self.computer_score = float(computer)
        self.english_score = float(english)
        self.total_score = (self.physics_score + self.chemistry_score +
                            self.maths_score + self.computer_score +
                            self.english_score)
        self.percentage = self.total_score / 5
        self.calculate_grade()

    def calculate_grade(self):
        if self.percentage >= 90:
            self.grade = "A1"
        elif self.percentage >= 80:
            self.grade = "A2"
        elif self.percentage >= 70:
            self.grade = "B1"
        elif self.percentage >= 60:
            self.grade = "B2"
        elif self.percentage >= 50:
            self.grade = "C1"
        elif self.percentage >= 40:
            self.grade = "C2"
        elif self.percentage >= 34:
            self.grade = "D1"
        else:
            self.grade = "E(FAILED)"

    def write_record(self, roll, name, physics, chemistry, maths, computer, english):
        try:
            rec = StudentRecord()
            rec.add_record(roll, name, physics, chemistry, maths, computer, english)
            with open("stud.dat", "ab") as file:
                pickle.dump(rec, file)
            status_label.config(text="Record added in file")
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}")

def clear_entries():
    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    physics_entry.delete(0, tk.END)
    chemistry_entry.delete(0, tk.END)
    maths_entry.delete(0, tk.END)
    computer_entry.delete(0, tk.END)
    english_entry.delete(0, tk.END)

def display_records():
    try:
        with open("stud.dat", "rb") as file:
            records = pickle.load(file)
            for record in records:
                print(record.roll_number, record.name, record.physics_score, record.chemistry_score, record.maths_score, record.computer_score, record.english_score, record.total_score, record.percentage, record.grade)
    except Exception as e:
        print(f"Error: {str(e)}")

def search_by_rollno(roll):
    try:
        with open("stud.dat", "rb") as file:
            records = pickle.load(file)
            for record in records:
                if record.roll_number == int(roll):
                    print(record.roll_number, record.name, record.physics_score, record.chemistry_score, record.maths_score, record.computer_score, record.english_score, record.total_score, record.percentage, record.grade)
    except Exception as e:
        print(f"Error: {str(e)}")

def search_by_name(name):
    try:
        with open("stud.dat", "rb") as file:
            records = pickle.load(file)
            for record in records:
                if record.name == name.upper():
                    print(record.roll_number, record.name, record.physics_score, record.chemistry_score, record.maths_score, record.computer_score, record.english_score, record.total_score, record.percentage, record.grade)
    except Exception as e:
        print(f"Error: {str(e)}")

def modify_by_rollno(roll):
    pass  # Implement modify functionality

def delete_by_rollno(roll):
    pass  # Implement delete functionality

root = tk.Tk()
root.title("Student Record Management")

tk.Label(root, text="Roll No:").grid(row=0, column=0, sticky="e")
tk.Label(root, text="Name:").grid(row=1, column=0, sticky="e")
tk.Label(root, text="Physics:").grid(row=2, column=0, sticky="e")
tk.Label(root, text="Chemistry:").grid(row=3, column=0, sticky="e")
tk.Label(root, text="Maths:").grid(row=4, column=0, sticky="e")
tk.Label(root, text="Computer:").grid(row=5, column=0, sticky="e")
tk.Label(root, text="English:").grid(row=6, column=0, sticky="e")
status_label = tk.Label(root, text="")
status_label.grid(row=8, columnspan=2)

roll_entry = tk.Entry(root)
name_entry = tk.Entry(root)
physics_entry = tk.Entry(root)
chemistry_entry = tk.Entry(root)
maths_entry = tk.Entry(root)
computer_entry = tk.Entry(root)
english_entry = tk.Entry(root)

roll_entry.grid(row=0, column=1)
name_entry.grid(row=1, column=1)
physics_entry.grid(row=2, column=1)
chemistry_entry.grid(row=3, column=1)
maths_entry.grid(row=4, column=1)
computer_entry.grid(row=5, column=1)
english_entry.grid(row=6, column=1)

record = StudentRecord()

add_button = tk.Button(root, text="Add Record", command=lambda: record.write_record(roll_entry.get(), name_entry.get(), physics_entry.get(), chemistry_entry.get(), maths_entry.get(), computer_entry.get(), english_entry.get()))
add_button.grid(row=7, column=0, columnspan=2, pady=10)

clear_button = tk.Button(root, text="Clear Entries", command=clear_entries)
clear_button.grid(row=9, column=0, columnspan=2, pady=10)

display_button = tk.Button(root, text="Display All Records", command=display_records)
display_button.grid(row=10, column=0, columnspan=2, pady=10)

search_rollno_button = tk.Button(root, text="Search by Roll No", command=lambda: search_by_rollno(roll_entry.get()))
search_rollno_button.grid(row=11, column=0, columnspan=2, pady=10)

search_name_button = tk.Button(root, text="Search by Name", command=lambda: search_by_name(name_entry.get()))
search_name_button.grid(row=12, column=0, columnspan=2, pady=10)

modify_button = tk.Button(root, text="Modify by Roll No", command=lambda: modify_by_rollno(roll_entry.get()))
modify_button.grid(row=13, column=0, columnspan=2, pady=10)

delete_button = tk.Button(root, text="Delete by Roll No", command=lambda: delete_by_rollno(roll_entry.get()))
delete_button.grid(row=14,
 column=0, columnspan=2, pady=10)

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.grid(row=15, column=0, columnspan=2, pady=10)

root.mainloop()
