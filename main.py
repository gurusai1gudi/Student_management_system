from database import create_enrollment_table
from student import add_student, show_students, delete_students, update_students,add_course,show_course,enroll_students,show_enrollments

#create_enrollment_table()
#print("created")

while True:
    print("\n1. Add student")
    print("2. Show students")
    print("3. Delete student")
    print("4. Update student")
    print("5. Add course")
    print("6. Show courses")
    print("7.enroll students")
    print("8. show_enrollments")
    print("9. exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        delete_students()
    elif choice == "4":
        update_students()
    elif choice == "5":
        add_course()
    elif choice=="6":
        show_course()
    elif choice == "7":
        enroll_students()
    elif choice == "8":
        show_enrollments()
    elif choice == "9":
        break
    else:
        print("Invalid choice")
