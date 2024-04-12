#Name: Jackson
#Date: 01/03/24
#Purpose: 2D List
list= self.get_from_db()

new_list = [list(ele) for ele in list]

grades= [["Ethan", 80,77,88,99],
         ["John", 60,88,95,70],
         ["Dylan", 75,59,65,79],
         ["Thomas", 95,99,85,89],
         ["Jerald", 85,88,72,69]]

def add():
    new_student = input("Please add a new student: ")
    gr1 = float(input("Please add grade 1 : "))
    gr2 = float(input("Please add grade 2 : "))
    gr3 = float(input("Please add grade 3 : "))
    gr4 = float(input("Please add grade 4 : "))

    grades.append([new_student,gr1,gr2,gr3,gr4])


def class_average(course):
    total=0
    for student in grades:
        total+=student[course]
    return total/len(grades)

def student_average(student):
    total=0
    total=grades[student][1]+grades[student][2]+grades[student][3]+grades[student][4]
    return total/4

def print_class_avg():
    print(f"Class 1 avg :{class_average(1)}")
    print(class_average(2))
    print(class_average(3))
    print(class_average(4))

def print_student_avg():
    for i in range(len(grades)):
        print(f"{grades[i][0]}'s avg is {student_average(i)}")     

options =["add","c avg","s avg","ext"]

menus = dict({"add":add, "c avg":print_class_avg,"s avg":print_student_avg,"ext":exit})
while True:
    
    choice = input("What is your choice:")
    if choice in options:
        menus[choice]()
    else:
        print("bad input")