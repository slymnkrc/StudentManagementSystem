from typing import Union

global studentlist
studentlist = ["john wick", "luiz gustavo", "suleyman karaca", "elon musk", "alan turing"]
a = 0
for i in range(3):
    print("name and surname:")
    studentname = input()

    if studentname in studentlist:
        print("welcome")
        break
    else:
        a = a + 1
if a == 3:
    print("please try again later")
    exit()
list_lessons = []
print("Do you want to continue with the course selection screen: YES or NO")
value = input()
if value == "YES":
    print("You must add 5 courses:")
    for i in range(5):
        list_lessons.append(input())
else:
    exit()
print("course selection screen")
list_number = range(5)

selected_courses = []

for i in range(5):
    print("continue with course selection: YES, finalize course selection: NO", )
    cont1 = input()
    if cont1 == "YES":
        print("0:", list_lessons[0], "1:", list_lessons[1], "2:", list_lessons[2], "3:", list_lessons[3], "4:",
              list_lessons[4])
        print("enter the course code(0-4) :")
        cont = input()
        if cont == "0" or "1" or "2" or "3" or "4":
            selected_courses.append(cont)
        else:
            print("wrong lesson code")
            continue
    else:
        break


def selected_lessons(b):
    if len(b) < 3:
        return print("you failed in class")


selected_lessons(selected_courses)
if len(selected_courses)<3:
    exit()

exam_notes = dict()
print("midterm grade")
exam_notes["midterm"] = input()
print("final grade")
exam_notes["final"] = input()
print("project grade")
exam_notes["project"] = input()

total = float(exam_notes["midterm"])*0.3+float(exam_notes["final"])*0.5+float(exam_notes["project"])*0.2
print(total)

if total>90:
    print("GRADE NOTE AA")
elif 70<total<90:
    print("GRADE NOTE BB")
elif 50<total<70:
    print("GRADE NOTE CC")
elif 30<total<50:
    print("GRADE NOTE DD")
elif total<30:
    print("GRADE NOTE FF")