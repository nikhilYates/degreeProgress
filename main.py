from multiprocessing.sharedctypes import Value
import math
import os
import time

gpa = {
    'A+': 9,
    'A': 8,
    'B+': 7,
    'B': 6,
    'C+': 5,
    'C': 4,
    'D+': 3,
    'D': 2,
    'E': 1,
    'F': 0,
    'P': 0
}

dict = {
    'PHYS-1411': {'GRADE': 'C', 'WEIGHT': 3},
    'MATH-1310': {'GRADE': 'A', 'WEIGHT': 3},
    'MATH-1300': {'GRADE': 'B+', 'WEIGHT': 3},
    'MATH-1021': {'GRADE': 'B', 'WEIGHT': 3},
    'CHEM-1000': {'GRADE': 'B+', 'WEIGHT': 3},
    'EECS-1012': {'GRADE': 'B+', 'WEIGHT': 3},
    'EECS-1001': {'GRADE': 'P', 'WEIGHT': 1},
    'SOCI-1010': {'GRADE': 'A', 'WEIGHT': 6},
    'EECS-1022':  {'GRADE': 'B+', 'WEIGHT': 3},
    'MATH-1019':  {'GRADE': 'B', 'WEIGHT': 3},
    'MATH-2030':  {'GRADE': 'D', 'WEIGHT': 3},
    'EECS-2031':  {'GRADE': 'B', 'WEIGHT': 3},
    'EECS-2030':  {'GRADE': 'C+', 'WEIGHT': 3},
    'EECS-2021':  {'GRADE': 'C', 'WEIGHT': 4},
    'EECS-2001':  {'GRADE': 'B+', 'WEIGHT': 3},
    'ECON-1000':  {'GRADE': 'A', 'WEIGHT': 3},
    'COMN-1000':  {'GRADE': 'A', 'WEIGHT': 6},
    'MATH-1090':  {'GRADE': 'B', 'WEIGHT': 3},
    'ENTR-3600':  {'GRADE': 'A', 'WEIGHT': 3},
    'ENTR-3400':  {'GRADE': 'A', 'WEIGHT': 3},
    'EECS-3421':  {'GRADE': 'C+', 'WEIGHT': 3},
    'EECS-3221':  {'GRADE': 'D+', 'WEIGHT': 3},
    'EECS-3215':  {'GRADE': 'B+', 'WEIGHT': 4},
    'EECS-3000':  {'GRADE': 'B', 'WEIGHT': 3},
    'EECS-2011':  {'GRADE': 'B', 'WEIGHT': 3},
    'EECS-3101':  {'GRADE': 'B+', 'WEIGHT': 3},
    'MATH-1581':  {'GRADE': ' ', 'WEIGHT': 3},
    'ENTR-4500':  {'GRADE': ' ', 'WEIGHT': 3},
    'EECS-4421':  {'GRADE': ' ', 'WEIGHT': 3},
    'EECS-4413':  {'GRADE': ' ', 'WEIGHT': 3},
    'EECS-4404':  {'GRADE': ' ', 'WEIGHT': 3},
    'EECS-4080':  {'GRADE': ' ', 'WEIGHT': 3},
    'EECS-3311':  {'GRADE': ' ', 'WEIGHT': 3},
    'SOCI-3410':  {'GRADE': ' ', 'WEIGHT': 6},
    'FR-1080': {'GRADE': ' ', 'WEIGHT': 6},
    'LAW-3591':  {'GRADE': ' ', 'WEIGHT': 3}
}

credCount = 120
username = 'nikhil'
password = '1234'
good_to_go = 0

print("Degree Progress for HBSc in Computer Science (2020-2024)"'\n')
time.sleep(2)



def gradePointAvg():
    culmin = 0
    completed_courses = 0
    for keys in dict:

        if keys == 'EECS-1001':

            culmin += 0
            completed_courses += 0
        else:
            if dict.get(keys, {}).get('GRADE') != ' ':

                culmin += gpa[dict.get(keys, {}).get('GRADE')] * dict.get(keys, []).get('WEIGHT')
                completed_courses += dict.get(keys, []).get('WEIGHT')

    rcgpa = round(culmin/completed_courses, 2)
    # print("CGPA = ", rcgpa, '\n')
    return rcgpa
def comprehensive():
    os.system('clear')
    print("OVERVIEW OF COURSES: 2020-2024"'\n')
    complete_courses = 0
    complete_credits = 0
    
    for keys in dict:
        if dict.get(keys, {}).get('GRADE') == ' ':
            print(keys, "-", "IN PROGRESS", "-", dict[keys]['WEIGHT'])
        else:
            print(keys, "-", dict[keys]['GRADE'], "-", dict[keys]['WEIGHT'])
            complete_courses += 1
            complete_credits += dict.get(keys, {}).get('WEIGHT')
        print("----------------------------")

    print()
    print("Courses Completed = ", complete_courses)
    print("Credits Received = ", complete_credits)
    print("Required Credits = ", credCount - complete_credits)

    grade = gradePointAvg()
    print("CGPA = ", grade)
    print()

    go_back = input("Return To Menu [b]"'\n'
                   "enter: ")
    if go_back == 'b':
        os.system('clear')
        return 1

def searchFunc():
    course = ''
    while course != 'b':
        os.system('clear')
        course = input("Enter the course following the format: XXXX-YYYY OR [b] to go back to menu"'\n'
                       "enter: ")
        if course == 'b':
            return 1

        if course not in dict:
            print("course not taken")
        else:
            print()
            print("GRADE =", dict.get(course, {}).get('GRADE'))
            print("-------------------------")
            print("GRADE CREDIT VALUE = ", gpa[dict.get(course, {}).get('GRADE')])
            print("-------------------------")
            print("COURSE CREDIT WEIGHT = ", dict.get(course, {}).get('WEIGHT'))
            print("-------------------------")

        print()
        restart = input("search for another course [n] or go back [b]"'\n'
                        "enter: ")
        if restart == 'n':
            continue
        if restart == 'b':
            return 1

wrong_user = -1
wrong_pass = -1
user = ''
pword = ''

while good_to_go == 0:
    os.system('clear')
    print("AUTHENTICATION")
    print("--------------")
    if wrong_user == -1:
        user = input("Enter Username: ")
    elif wrong_user == 1:
        print("Enter a correct Username")
        user = input("Enter Username: ")
    elif wrong_user == 0:
        print("Enter Username: ", user)

    if user != username:
        wrong_user = 1
        user = ''
        continue
    else:
        wrong_user = 0
    if wrong_pass == -1:
        pword = input("Enter Password: ")
    elif wrong_pass == 1:
        print("Incorrect Password")
        pword = input("Enter Password: ")

    if pword != password:
        wrong_pass = 1
        continue
    else:
        good_to_go = 1

while 1:
    os.system('clear')
    print("MENU")
    print("------------------------")
    print()
    selection = input("Comprehensive Report [1]"'\n'
                      "BEST Checklist       [2]"'\n'
                      "EECS Checklist       [3]"'\n'
                      "GPA                  [4]"'\n'
                      "Search Course        [5]"'\n''\n'
                      "enter: ")
    sel_num = int(selection)

    if sel_num < 1 or sel_num > 5:
        print("Enter a valid selection")

    if sel_num == 1:
        comprehensive()
    if sel_num == 4:
        gradePointAvg()
    if sel_num == 5:
        searchFunc()





