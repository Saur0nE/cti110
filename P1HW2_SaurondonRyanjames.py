#Saurondon Ryanjames
#2023/11/09
#Strings and Integars

#header
print("This program calculates and displays travel expense")

#User input Data
budget1 = int(input("Enter Budget: "))
place1 =(input("Enter your travel destination: "))
gas1 = int(input("How much do you think will spend on gas? "))
hotel1 = int(input("Approximately, how much will you need for accomodation/hotel? "))
food1 = int(input("Last, how much do you need for food? "))

#Display Output
print("------------Travel Expenses------------")
print("location: ", place1)
print("Initial Budget: ", budget1)

print("Fuel: ", gas1)
print("Accomodation: ", hotel1)
print("Food: ", food1)

#Total Number Output
print("Remaining Balance: ", (budget1) - (gas1) - (hotel1) - (food1))
