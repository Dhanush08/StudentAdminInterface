from MainPackage import Student, Admin
while True:
    user = int(input("""Enter choice
    1.Student
    2.Admin
    3.Exit """))
    if user is 1:
        Student.display_student()
    elif user is 2:
        start = True
        while start:
            username = input('Enter you username ')
            user_password = input('Enter your password ')
            if Admin.user_name(username, user_password):
                while True:
                    choice = int(input(f"""Welcome! {username} 
                    Menu:
                    1.Add Student
                    2.Delete Student
                    3.Display Student
                    4.Display Student list
                    5.Logout
                    6.Exit """))
                    if choice is 1:
                        Student.add_student()
                    if choice is 2:
                        Student.delete_student()
                    if choice is 3:
                        Student.display_student()
                    if choice is 4:
                        Student.display()
                    if choice is 5:
                        start = False
                        break
                    if choice is 6:
                        quit(0)
            else:
                print("Invalid Username or Password")
    elif user is 3:
        quit(0)
    else:
        print("Enter valid option ")
