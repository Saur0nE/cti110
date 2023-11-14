#Saurondon Ryanjames
#2023/11/14
#Use float values to represent the cost to drive a specified distance

#Get input from user
mpg = float(input("Enter car's MPG as a decimal: "))
cost_gal = float(input("Enter the cost for one gallon of gas: "))

#Calculate cost to drive 20 miles
mile_cost_20 = (mpg/20) * cost_gal

#Calculate cost to drive 75 miles
mile_cost_75 = (75/mpg) * cost_gal

#Calculate cost to drive 500 miles
mile_cost_500 = (500/mpg) * cost_gal

#Output the cost with 2 decimal places using an f-string
print(f"Cost to drive 20 miles is {mile_cost_20:.2f}")

#Output the cost with 2 decimal places using an f-string
print(f"Cost to drive 75 miles is {mile_cost_75:.2f}")

#Output the cost with 2 decimal places using an f-string
print(f"Cost to drive 500 miles is {mile_cost_500:.2f}")
