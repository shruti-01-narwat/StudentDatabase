
# Student Database Management System

## Description
This project is a Student Database Management System implemented using Python and MySQL. The system allows you to add, display, search, modify, and delete student records through a graphical user interface (GUI) built with Tkinter.

## Features
- **Add Record:** Add a new student record to the database.
- **Display All Records:** Display all student records in the database.
- **Search by Roll Number:** Search for a student record by roll number.
- **Search by Name:** Search for a student record by name.
- **Modify by Roll Number:** Modify an existing student record using the roll number.
- **Delete by Roll Number:** Delete a student record using the roll number.
- **Exit:** Exit the application.

## Prerequisites
- Python 3.x
- MySQL server
- MySQL Connector for Python

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/shruti-01-narwat/StudentDatabase
   ```

2. **Install required Python packages:**
   ```sh
   pip install mysql-connector-python
   ```

3. **Set up the MySQL database:**
   - Start your MySQL server.
   - Create a database:
     ```sql
     CREATE DATABASE student_db;
     ```
   - Use the created database:
     ```sql
     USE student_db;
     ```
   - Create the `students` table:
     ```sql
     CREATE TABLE students (
         roll_number INT PRIMARY KEY,
         name VARCHAR(100),
         physics_score FLOAT,
         chemistry_score FLOAT,
         maths_score FLOAT,
         computer_score FLOAT,
         english_score FLOAT,
         total_score FLOAT,
         percentage FLOAT,
         grade CHAR(2)
     );
     ```

## Usage
1. **Run the main script:**
   ```sh
   python main.py
   ```

2. **Interacting with the GUI:**
   - **Add Record:** Fill in the student details and click "Add Record" to add a new student to the database.
   - **Display All Records:** Click "Display All Records" to view all student records.
   - **Search by Roll Number:** Enter the roll number and click "Search by Roll No" to search for a specific student.
   - **Search by Name:** Enter the name and click "Search by Name" to search for a specific student.
   - **Modify by Roll Number:** Enter the roll number and new details, then click "Modify by Roll No" to update a student's information.
   - **Delete by Roll Number:** Enter the roll number and click "Delete by Roll No" to remove a student from the database.
   - **Exit:** Click "Exit" to close the application.

## File Structure
- `main.py`: Main entry point of the application.
- `gui.py`: Contains the `GUI` class which manages the Tkinter GUI and database operations.
- `student.py`: Contains the `Student` class which defines the student entity and related operations.


## Acknowledgements
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Python's de-facto standard GUI package.
- [MySQL](https://www.mysql.com/) - The world's most popular open source database.
- [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/) - MySQL driver written in Python.



