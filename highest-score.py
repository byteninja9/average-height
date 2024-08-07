student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Initialize the highest score variable
highest_score = 0

# Loop through the scores to find the highest one
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is {highest_score}.")
