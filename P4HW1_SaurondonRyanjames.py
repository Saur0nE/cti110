#Saurondon Ryanjames
#2023/11/30
#Use loop to get user input

from statistics import mean

num_grades = int(input("How many grades will you enter? "))

#create a list to store the grades entered
grades_list = []

#get grades from user
for i in range (num_grades):
    grade = float(input(f"Enter grade for Module {i + 1}: "))
    while grade < 0 or grade > 100:
        print("You entered an invalid grade: ")
        grade = float(input(f"Enter grade for Module {i + 1}: "))
    grades_list.append(grade)

print(grades_list)

#call methods on the list to get results
lowest_grade = min(grades_list)
highest_grade = max(grades_list)
list_sum = sum(grades_list)
list_avg = mean(grades_list)

#create a value for spacing
x = " "

#result table
print("\n")
print("------------------results------------------")
print("Lowest grade: ",  '      ', grades_list)
print("Highest grade: ", '      ', grades_list)
print("Sum of grades: ", '      ', f"{list_sum:.2f}")
print("Average: ", '            ', f"{list_avg:.2f}") 
print("--------------------------------------------")


