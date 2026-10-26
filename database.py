import sqlite3

class Database:
    def __init__(self):
        self.conn=sqlite3.connect("Student.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY ,name TEXT , lastname TEXT , password TEXT , course TEXT)""")
        self.conn.commit()

    def add_student(self , name,lastname,password,course):
        self.cursor.execute("""INSERT INTO student(name , lastname , password,course)VALUES (?,?,?,?)""",(name ,lastname,password,course))
        self.conn.commit()

    def select_record(self):
        self.cursor.execute("SELECT * FROM student")
        records = self.cursor.fetchall()
        return records

    def show_student(self):
        self.cursor.execute("SELECT * FROM student")
        return self.cursor.fetchall()
    
    def delete_student(self , student_id):
        self.cursor.execute("DELETE FROM student WHERE id=?" , (student_id,))
        self.conn.commit()

    def check_login(self , password):
        self.cursor.execute("SELECT * FROM student WHERE password=?" ,
                            (password,))
        return self.cursor.fetchone()
        