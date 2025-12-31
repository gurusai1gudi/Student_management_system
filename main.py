from database import alter_course
from student import add_student, show_students, delete_students, update_students, add_course, show_course, \
    enroll_students, show_enrollments, update_course_fee, pay_fee, show_course_access, access_course

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
    print("9. update fee")
    print("10. pay fee")
    print("11. show course access")
    print("12. access course")
    print("13. exit")
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
    elif choice=="9":
        update_course_fee()
    elif choice=="10":
        pay_fee()
    elif choice=="11":
        show_course_access()
    elif choice=="12":
        access_course()
    elif choice == "13":
        break
    else:
        print("Invalid choice")
