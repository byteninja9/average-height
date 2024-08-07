student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
#print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height

number_student = len(student_heights)
average_height = round(total_height / number_student)
print(average_height)
