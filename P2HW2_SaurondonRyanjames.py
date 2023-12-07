# CTI-110
# P2HW2 - List
# Saurondon Ryanjames
# 11/14/2023

from statistics import mean

#user inputs grades for each module
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

#Grades empty list
grade_list = []

#Values added to the list
grade_list.append(grade1)
grade_list.append(grade2)
grade_list.append(grade3)
grade_list.append(grade4)
grade_list.append(grade5)
grade_list.append(grade6)

#Display Output
print("------------Results------------")

#Lowest Grade
lowest_grade = min(grade_list)
print(f"Lowest Grade:      {lowest_grade:.2f}")
#Highest Grade
highest_grade = max(grade_list)
print(f"Highest Grade:     {highest_grade:.2f}")
#Sum of Grades
total_grade = sum(grade_list)
print(f"Sum of Grades:     {total_grade:.2f}")
#Average Grade
average_grade = mean(grade_list)
print(f"Average:     {average_grade:.2f}")

print("-------------------------------")
