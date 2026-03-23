'''def star_pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print(j+1,end = "")
         print()
star_pattern(5)'''


student_name=""
student_status=""
def show_menu():
    print("\n-----Attendance Tracker------")
    print("1. Add Attendance")
    print("2. view Attendance")
    print("3. Exit")
def add_attendance():
    global student_name
    global student_status

    student_name=input("Enter student name")
    student_status=input("Enter status (present/Absent)")
    print("Attendance added successfully")

def view_student():
    if student_name== "":
        print(student_name, "-" ,student_status)
def main():
    while True:
        show_menu()
        choice=input("Enter your choice")
        if choice=="1":
            add_attendance()
        elif choice=="2":
            view_attendance()
        elif choice=="3":
            print("Existing the program")
            break
        else:
            print("Invalid choice. Try again")
main()
