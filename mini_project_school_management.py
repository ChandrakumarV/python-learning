import os
import subprocess


def clear_console():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True, check=False)


staffs = ["Staff_1", "Staff_2", "Staff_3"]
students = ["Student_1", "Student_2", "Student_3"]


service = """
0.Exit
1.Staff Management
2.Student Management
"""

list_staff = """
0.Exit
1.List Staffs
2.Add Staff
3.Delete Staff
4.Update Staff
5.Back
"""

list_student = """
0.Exit
1.List Students
2.Add Student
3.Delete Student
4.Update Student
5.Back
"""
# ---------------


def list_service():
    clear_console()
    print(service)
    return int(input("Option : "))


def list_staff_services():
    session = True
    while session:
        clear_console()
        print(list_staff)
        opt = int(input("Option : "))
        match opt:
            case 0:
                return 0
            case 1:  # List staff
                for st in staffs:
                    print(st)
                print("(press any key to return...)")
                input()
            case 2:  # Add staff
                name = input("Enter a staff name : ")
                staffs.append(name)
                print(f"{name} - Added (press any key to return...)")
                input()
            case 3:  # Delete staff
                for i, staff in enumerate(staffs):
                    print(i + 1, " - ", staff)
                staff_no = int(input("Enter staff no : "))
                name = staffs[staff_no - 1]
                staffs.pop(staff_no - 1)
                print(f"{name} - Deleted... (press any key to return)")
                input()
            case 4:  # Update staff
                for i, staff in enumerate(staffs):
                    print(i + 1, " - ", staff)
                staff_no = int(input("Enter staff no : "))
                name = staffs[staff_no - 1]
                new_name = input(f"Enter a new name for {name} : ")
                staffs[staff_no - 1] = new_name
                print(f"{name} -> {new_name} - Updated (press any key to return...)")
                input()
            case 5:
                break


def list_student_management():
    session = True
    while session:
        clear_console()
        print(list_student)
        opt = int(input("Option : "))
        match opt:
            case 0:
                return 0
            case 1:  # List Student
                for st in students:
                    print(st)
                print("(press any key to return...)")
                input()
            case 2:  # Add student
                name = input("Enter a student name : ")
                students.append(name)
                print(f"{name} - Added (press any key to return...)")
                input()
            case 3:  # Delete student
                for i, student in enumerate(students):
                    print(i + 1, " - ", student)
                student_no = int(input("Enter student no : "))
                name = students[student_no - 1]
                students.pop(student_no - 1)
                print(f"{name} - Deleted... (press any key to return)")
                input()
            case 4:  # Update student
                for i, student in enumerate(students):
                    print(i + 1, " - ", student)
                student_no = int(input("Enter student no : "))
                name = students[student_no - 1]
                new_name = input(f"Enter a new name for {name} : ")
                students[student_no - 1] = new_name
                print(f"{name} -> {new_name} - Updated (press any key to return...)")
                input()
            case 5:
                break


def main():
    session = True
    while session:
        opt = list_service()
        match opt:
            case 0:
                session = False
                break

            case 1:
                stafOpt = list_staff_services()
                if stafOpt == 0:
                    session = False
                    break

            case 2:
                studOpt = list_student_management()
                if studOpt == 0:
                    session = False
                    break


main()
