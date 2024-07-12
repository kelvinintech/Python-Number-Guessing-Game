import random

#The import statement in Python is used to include the funcitonality of external modules and libraries into your script, allowing you to 
# use functions, classes, and variables defined in those modules
#when you use the import statement, you are telling Python to load a module and make its contents availble for use in your script


def main():
    number_to_guess = random.raninint(1, 100)
    attempts = 0
   #main(): this function contains the main logic of the game
   #number_to_guess: Generates a random number interger between 1 and 100
   #attempts: A counter to keep track of the number attempts the player has name


    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess what is is?")
    #print: Prints the welcome message and instructions for the game. 

    while True:
        #this loop runs indefinitely unil the player guesses the correct number
        guess = input("Enter your guess: ")
        #guess = input(""): Prompts the player to enter their guess
        

        if not guess.isdigit():
            #checks if the input is a valid number.
            print("Please enter a valid number.")
            
            continue

            guess = int(guess)
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again")
            else:
                print("Congratulations! You guessed the number in {attempts} attempts.")
                break

            if _name_ == "_main_":
                main()


#import is 