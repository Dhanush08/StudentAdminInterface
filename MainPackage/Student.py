import re
student_list = []


def add_student():
    name = input('Enter student name ')
    roll_no_pattern = re.compile("^[1-9][0-9A-Z]{9}")
    roll_no = input(f"Enter {name}'s roll number ")
    while True:
        if re.match(roll_no_pattern, roll_no):
            while True:
                for i in range(len(student_list)):
                    if student_list[i]["Roll_number"] == roll_no and re.match(roll_no_pattern, roll_no):
                        print('This Roll number is already registered in another profile ')
                        roll_no = input(f"Enter {name}'s roll number again ")
                        break
                    elif not re.match(roll_no_pattern, roll_no):
                        print('Something is wrong in the roll number')
                        roll_no = input(f"Enter {name}'s roll number again ")
                        break
                else:
                    break
            break
        else:
            print('Something is wrong in the roll number')
            roll_no = input(f"Enter {name}'s roll number again ")
    branch_pattern = re.compile("(CSE|ECE|MEC|EEE|IT)")
    branch = input(f"Enter {name}'s branch ").upper()
    while True:
        if re.match(branch_pattern, branch):
            break
        else:
            print('Not a branch')
            branch = input(f"Enter {name}'s branch again ")
    year_pattern = re.compile(r"^[1-9]\d{3}")
    year = input(f"Enter {name}'s academic year ")
    while True:
        if re.match(year_pattern, year):
            break
        else:
            print('Invalid year')
            year = input(f"Enter {name}'s academic year again ")
    dictionary = {
        "Name": name,
        "Roll_number": roll_no,
        "Branch": branch,
        "Year": year
    }
    student_list.append(dictionary)
    print(f"{name} is registered successfully")


def delete_student():
    roll_no_pattern = re.compile("^[1-9][0-9A-Z]{9}")
    roll_no = input(f"Enter roll number to delete ")
    while True:
        if re.match(roll_no_pattern, roll_no):
            break
        else:
            print('Something is wrong in the roll number')
            roll_no = input(f"Enter roll number again ")
    for student_details in student_list:
        if roll_no == student_details["Roll_number"]:
            print(f"{student_details['Name']}'s profile is deleted ")
            student_list.remove(student_details)
            break
    else:
        print('No such profile with roll number to delete')


def display_student():
    roll_no_pattern = re.compile("^[1-9][0-9A-Z]{9}")
    roll_no = input(f"Enter roll number to display profile ")
    while True:
        if re.match(roll_no_pattern, roll_no):
            break
        else:
            print('Something is wrong in the roll number')
            roll_no = input(f"Enter roll number again ")
    for student_details in student_list:
        if roll_no == student_details["Roll_number"]:
            print(f"""{student_details['Name']}'s profile: 
            Name        : {student_details['Name']}
            Roll Number : {student_details['Roll_number']}
            Branch      : {student_details['Branch']}
            Year        : {student_details['Year']}""")
            break
    else:
        print('No such profile with roll number to display')


def display():
    if student_list:
        for student_details in student_list:
            print(f"""{student_details['Name']}'s profile: 
            Name        : {student_details['Name']}
            Roll Number : {student_details['Roll_number']}
            Branch      : {student_details['Branch']}
            Year        : {student_details['Year']}""")
    else:
        print("No student profiles registered")
