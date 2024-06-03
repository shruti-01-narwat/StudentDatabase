import tkinter as tk
import mysql.connector
from gui import GUI

def main():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='studentdb',
                                             user='root',
                                             password='Shiv2003@#')
        if connection.is_connected():
            print("Connected to MySQL database")

            cursor = connection.cursor()

            create_table_query = """
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                physics_score FLOAT NOT NULL,
                chemistry_score FLOAT NOT NULL,
                maths_score FLOAT NOT NULL,
                computer_score FLOAT NOT NULL,
                english_score FLOAT NOT NULL,
                total_score FLOAT NOT NULL,
                percentage FLOAT NOT NULL,
                grade VARCHAR(10) NOT NULL
            )
            """

            cursor.execute(create_table_query)
            connection.commit()

            root = tk.Tk()
            app = GUI(root)
            root.mainloop()

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    main()
