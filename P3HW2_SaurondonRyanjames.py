#Saurond Ryanjames
#2023/11/21
#Use if/else to determine an employees pay

#Get User Input
emp_name = input("Enter employee's name: ")
emp_hours = float(input("Enter employee's hours worked: "))
emp_pay = float(input("Enter employee's pay rate: "))

#Calculaions
if emp_hours > 40:
    ot_hours = emp_hours - 40
    reg_hours = 40

#This represents if emp_hours is 40 or less
else:
    ot_hours = 0
    reg_hours = emp_hours

#calulate pay
ot_pay = (emp_pay * 1.5) * ot_hours
reg_pay = emp_pay * reg_hours
gross_pay = ot_pay + reg_pay

#Display results
print("----------------------------------------")
print("Employee name: ", emp_name)

print("\n", "Hours worked   ", "Pay Rate   ", "OverTime Pay   ", "RegHour Pay   ", "Gross Pay")
print("--------------------------------------------------------------------------------")
print(f"{emp_hours:8.1f} {emp_pay:13.1f} {ot_pay:14.1f} {reg_pay:15.2f} {gross_pay:15.2f}")
