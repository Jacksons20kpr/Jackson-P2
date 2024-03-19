#Name: Jackson
#Date: 01/03/24
#Purpose: 2D List
grades= [["Ethan", 80,77,88,99],
         ["John", 60,88],
         ["Dylan", 75,21],
         ["Thomas", 95,99],
         ["Jerald", 85,88]]
#new_student = input("Please add a new student: ")
#grades.append(new_student)
def class_average(course):
    total=0
    for student in grades:
        total+=student[course]
    return total/len(grades)

def student_average(student):
    total=0
    total=grades[student][1]+grades[student][2]+grades[student][3]+grades[student][4]
    return total/4

print(class_average(2))
print(student_average(0))     
