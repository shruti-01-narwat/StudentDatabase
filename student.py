<<<<<<< HEAD
import mysql.connector

class Student:
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

    def add_record(self):
        try:
            connection = connect_to_database()
            cursor = connection.cursor()

            sql = "INSERT INTO students (name, physics_score, chemistry_score, maths_score, computer_score, english_score, total_score, percentage, grade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (self.name, self.physics_score, self.chemistry_score, self.maths_score, self.computer_score, self.english_score, self.total_score, self.percentage, self.grade)

            cursor.execute(sql, values)
            connection.commit()

            print("Record added successfully!")

        except mysql.connector.Error as error:
            print("Error:", error)

        finally:
            if connection.is_connected():
                cursor.close()
                close_connection(connection)

    def get_all_records(self):
        try:
            connection = connect_to_database()
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM students")
            records = cursor.fetchall()

            for record in records:
                print(record)

        except mysql.connector.Error as error:
            print("Error:", error)

        finally:
            if connection.is_connected():
                cursor.close()
                close_connection(connection)

def connect_to_database():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='studentdb',
                                             user='root',
                                             password='********')
        return connection
    except mysql.connector.Error as error:
        print("Error:", error)

def close_connection(connection):
    connection.close()

# Add other utility functions as needed

# Test the Student class
if __name__ == "__main__":
    student1 = Student()
    student1.name = "John Doe"
    student1.physics_score = 85
    student1.chemistry_score = 90
    student1.maths_score = 78
    student1.computer_score = 92
    student1.english_score = 88
    student1.total_score = (student1.physics_score + student1.chemistry_score +
                            student1.maths_score + student1.computer_score +
                            student1.english_score)
    student1.percentage = student1.total_score / 5
    if student1.percentage >= 90:
        student1.grade = "A1"
    elif student1.percentage >= 80:
        student1.grade = "A2"
    elif student1.percentage >= 70:
        student1.grade = "B1"
    elif student1.percentage >= 60:
        student1.grade = "B2"
    elif student1.percentage >= 50:
        student1.grade = "C1"
    elif student1.percentage >= 40:
        student1.grade = "C2"
    elif student1.percentage >= 34:
        student1.grade = "D1"
    else:
        student1.grade = "E(FAILED)"

    student1.add_record()

    student2 = Student()
    student2.name = "Jane Smith"
    student2.physics_score = 92
    student2.chemistry_score = 88
    student2.maths_score = 80
    student2.computer_score = 85
    student2.english_score = 90
    student2.total_score = (student2.physics_score + student2.chemistry_score +
                            student2.maths_score + student2.computer_score +
                            student2.english_score)
    student2.percentage = student2.total_score / 5
    if student2.percentage >= 90:
        student2.grade = "A1"
    elif student2.percentage >= 80:
        student2.grade = "A2"
    elif student2.percentage >= 70:
        student2.grade = "B1"
    elif student2.percentage >= 60:
        student2.grade = "B2"
    elif student2.percentage >= 50:
        student2.grade = "C1"
    elif student2.percentage >= 40:
        student2.grade = "C2"
    elif student2.percentage >= 34:
        student2.grade = "D1"
    else:
        student2.grade = "E(FAILED)"

    student2.add_record()

    student1.get_all_records()
=======
import mysql.connector

class Student:
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

    def add_record(self):
        try:
            connection = connect_to_database()
            cursor = connection.cursor()

            sql = "INSERT INTO students (name, physics_score, chemistry_score, maths_score, computer_score, english_score, total_score, percentage, grade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (self.name, self.physics_score, self.chemistry_score, self.maths_score, self.computer_score, self.english_score, self.total_score, self.percentage, self.grade)

            cursor.execute(sql, values)
            connection.commit()

            print("Record added successfully!")

        except mysql.connector.Error as error:
            print("Error:", error)

        finally:
            if connection.is_connected():
                cursor.close()
                close_connection(connection)

    def get_all_records(self):
        try:
            connection = connect_to_database()
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM students")
            records = cursor.fetchall()

            for record in records:
                print(record)

        except mysql.connector.Error as error:
            print("Error:", error)

        finally:
            if connection.is_connected():
                cursor.close()
                close_connection(connection)

def connect_to_database():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='student_records',
                                             user='your_username',
                                             password='your_password')
        return connection
    except mysql.connector.Error as error:
        print("Error:", error)

def close_connection(connection):
    connection.close()

# Add other utility functions as needed

# Test the Student class
if __name__ == "__main__":
    student1 = Student()
    student1.name = "John Doe"
    student1.physics_score = 85
    student1.chemistry_score = 90
    student1.maths_score = 78
    student1.computer_score = 92
    student1.english_score = 88
    student1.total_score = (student1.physics_score + student1.chemistry_score +
                            student1.maths_score + student1.computer_score +
                            student1.english_score)
    student1.percentage = student1.total_score / 5
    if student1.percentage >= 90:
        student1.grade = "A1"
    elif student1.percentage >= 80:
        student1.grade = "A2"
    elif student1.percentage >= 70:
        student1.grade = "B1"
    elif student1.percentage >= 60:
        student1.grade = "B2"
    elif student1.percentage >= 50:
        student1.grade = "C1"
    elif student1.percentage >= 40:
        student1.grade = "C2"
    elif student1.percentage >= 34:
        student1.grade = "D1"
    else:
        student1.grade = "E(FAILED)"

    student1.add_record()

    student2 = Student()
    student2.name = "Jane Smith"
    student2.physics_score = 92
    student2.chemistry_score = 88
    student2.maths_score = 80
    student2.computer_score = 85
    student2.english_score = 90
    student2.total_score = (student2.physics_score + student2.chemistry_score +
                            student2.maths_score + student2.computer_score +
                            student2.english_score)
    student2.percentage = student2.total_score / 5
    if student2.percentage >= 90:
        student2.grade = "A1"
    elif student2.percentage >= 80:
        student2.grade = "A2"
    elif student2.percentage >= 70:
        student2.grade = "B1"
    elif student2.percentage >= 60:
        student2.grade = "B2"
    elif student2.percentage >= 50:
        student2.grade = "C1"
    elif student2.percentage >= 40:
        student2.grade = "C2"
    elif student2.percentage >= 34:
        student2.grade = "D1"
    else:
        student2.grade = "E(FAILED)"

    student2.add_record()

    student1.get_all_records()
>>>>>>> ad5be716e64d69f5d0f01abfd27ee5921e541a48
