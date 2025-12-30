import sqlite3

def connect_db():
    conn = sqlite3.connect("students.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT,
        email TEXT
    )
    """)
    conn.commit()
    conn.close()
def create_course_table():
    conn=connect_db()
    cursor=conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses(
     id INTEGER PRIMARY KEY,
     course_name TEXT NOT NULL
     )
    """)

def create_enrollment_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollments (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
    """)

    conn.commit()
    conn.close()
