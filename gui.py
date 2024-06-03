import tkinter as tk
from tkinter import messagebox
import mysql.connector

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Record Management")
        self.root.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        self.label_name = tk.Label(self.root, text="Name:")
        self.label_name.grid(row=0, column=0, sticky="e")
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1)

        self.label_physics = tk.Label(self.root, text="Physics Score:")
        self.label_physics.grid(row=1, column=0, sticky="e")
        self.entry_physics = tk.Entry(self.root)
        self.entry_physics.grid(row=1, column=1)

        self.label_chemistry = tk.Label(self.root, text="Chemistry Score:")
        self.label_chemistry.grid(row=2, column=0, sticky="e")
        self.entry_chemistry = tk.Entry(self.root)
        self.entry_chemistry.grid(row=2, column=1)

        self.label_maths = tk.Label(self.root, text="Maths Score:")
        self.label_maths.grid(row=3, column=0, sticky="e")
        self.entry_maths = tk.Entry(self.root)
        self.entry_maths.grid(row=3, column=1)

        self.label_computer = tk.Label(self.root, text="Computer Score:")
        self.label_computer.grid(row=4, column=0, sticky="e")
        self.entry_computer = tk.Entry(self.root)
        self.entry_computer.grid(row=4, column=1)

        self.label_english = tk.Label(self.root, text="English Score:")
        self.label_english.grid(row=5, column=0, sticky="e")
        self.entry_english = tk.Entry(self.root)
        self.entry_english.grid(row=5, column=1)

        self.button_add_record = tk.Button(self.root, text="Add Record", command=self.add_record)
        self.button_add_record.grid(row=6, columnspan=2, pady=10)

    def add_record(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='student_records',
                                                 user='your_username',
                                                 password='your_password')
            cursor = connection.cursor()

            name = self.entry_name.get()
            physics_score = float(self.entry_physics.get())
            chemistry_score = float(self.entry_chemistry.get())
            maths_score = float(self.entry_maths.get())
            computer_score = float(self.entry_computer.get())
            english_score = float(self.entry_english.get())
            total_score = physics_score + chemistry_score + maths_score + computer_score + english_score
            percentage = total_score / 5
            if percentage >= 90:
                grade = "A1"
            elif percentage >= 80:
                grade = "A2"
            elif percentage >= 70:
                grade = "B1"
            elif percentage >= 60:
                grade = "B2"
            elif percentage >= 50:
                grade = "C1"
            elif percentage >= 40:
                grade = "C2"
            elif percentage >= 34:
                grade = "D1"
            else:
                grade = "E(FAILED)"

            sql = "INSERT INTO students (name, physics_score, chemistry_score, maths_score, computer_score, english_score, total_score, percentage, grade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (name, physics_score, chemistry_score, maths_score, computer_score, english_score, total_score, percentage, grade)

            cursor.execute(sql, values)
            connection.commit()

            messagebox.showinfo("Success", "Record added successfully!")

        except mysql.connector.Error as error:
            messagebox.showerror("Error", str(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
