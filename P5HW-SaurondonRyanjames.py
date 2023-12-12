#Saurondon Ryanjames
#2023-12-09
#Functions, random numbers, and while loops

#Import random library
import random

#This function displays the main menu
def show_menu():
        print("Welcome to Math Quiz")
        print()
        print()
        print("----------MAIN MENU----------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        print()
        print()
   
#This function adds random numbers
def add():
    ran_num1 = random.randint(0, 10)
    ran_num2 = random.randint(0, 10)
    print(f"{ran_num1} + {ran_num2}")
    return (ran_num1 + ran_num2)

#This function subtracts random numbers
def subtract():
    ran_num1 = random.randint(0, 10)
    ran_num2 = random.randint(0, 10)
    print(f"{ran_num1} - {ran_num2}")
    return (ran_num1 - ran_num2)

#This function defines the user guessing the answer. While the user inputs
#the wrong answer, allow the user to guess again until correct.
def guessing(guess, correct_answer):
    num_guesses = 0
    while guess != correct_answer:
        num_guesses += 1
        if guess > correct_answer:
            print("your guess is too high. Try again!")
            guess = int(input("Guess again: "))
#If guess is too low or too high
        else:                             
             print("your guess is too low. Try again!")
             guess = int(input("What is your guess? "))
#Guess is correct, the while loop breaks
    else: 
        print("Your guess is correct!")
        print(f"Number of guesses: {num_guesses} total of incorrect guesses! ")

#Main function
def main():
    show_menu()
    user_option = int(input("Please choose one of the menu options: "))
    while user_option != 3:
            
            if user_option == 1:
                ran_sum = add()   #Represents the correct answer
                my_guess = int(input("Enter your guess: ")) 
                guessing (my_guess, ran_sum)
                print()
                show_menu()
                user_option = int(input("Please choose one of the menu options: "))

            if user_option == 2:
                ran_sum = subtract()   #Represents the correct answer
                my_guess = int(input("Enter your guess: ")) 
                guessing (my_guess, ran_sum)
                print()
                show_menu()
                user_option = int(input("Please choose one of the menu options: "))

     #if user_choise == 3, the while loop breaks
    print("Thank you for playing, goodbye!")

    
#Call main function
if __name__ == "__main__":
    main()
