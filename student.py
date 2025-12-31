from database import connect_db
def add_student():
    name = input("Enter your name:")
    course = input("Enter your course:")
    age = int(input("Enter your age:"))
    email = input("Enter your email:")
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students (name, course, age, email)
    VALUES (?, ?, ?, ?)
    """, (name, course, age, email))

    conn.commit()
    conn.close()

    print("added")
def show_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    if not students:
        print("No students found")
        return

    print("\n--- Student List ---")
    for student in students:
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")
        print(f"Course: {student[3]}")
        print(f"Email: {student[4]}")
        print("--------------------")

def delete_students():
    conn=connect_db()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM students")
    students= cursor.fetchall()
    conn.commit()
    conn.close()
    for student in students:
        student.remove()
    print("deleted")
def update_students():
    student_id = int(input("Enter student ID to update: "))
    new_name = input("Enter new name: ")
    new_course = input("Enter new course: ")
    new_age = int(input("Enter new age: "))
    new_email = input("Enter new email: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE students SET name=?,course=?,age=?,email=?
    WHERE id=?
    """,(new_name, new_course, new_age, new_email, student_id))
    conn.commit()
    conn.close()
#### _____________course_____________
def add_course():
    course_name = input("Enter course name: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO courses (course_name) VALUES(?)
                   """,(course_name,))
    conn.commit()
    conn.close()
    print("course added succesfully")

def show_course():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    conn.close()
    if not courses:
        print("No courses found")
    print("list of courses")
    for course in courses:
        print(f"ID: {course[0]}")
        print(f"Name: {course[1]}")
def enroll_students():
    student_id = int(input("Enter student ID to enroll: "))
    course_id = int(input("Enter course ID: "))
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id from students WHERE id=?", (student_id,))
    student = cursor.fetchone()
    if student is None:
        print("student not found")
        conn.close()
        return
    cursor.execute("SELECT id from courses WHERE id=?", (course_id,))
    course = cursor.fetchone()
    if course is None:
        print("course not found")
        conn.close()
        return
    cursor.execute(
        "SELECT id FROM enrollments WHERE student_id=? AND course_id=?",
        (student_id, course_id)
    )
    existing = cursor.fetchone()

    if existing is not None:
        print("Student already enrolled in this course")
        conn.close()
        return
    cursor.execute("""
    INSERT INTO enrollments (
    student_id,course_id)VALUES(?,?)""",
                   (student_id,course_id))
    conn.commit()
    conn.close()
    print("enrolled_succesfully")
def show_enrollments():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT students.name,courses.course_name
    FROM enrollments
    JOIN students ON enrollments.student_id = students.id
    JOIN courses ON enrollments.course_id = courses.id""")
    enrollments = cursor.fetchall()
    conn.close()
    for student_name, course_name in enrollments:
        print(f"{student_name}->{course_name}")







