import random

# Define a function that generates a random number between 1 and 100
def generate_random_number():
    return random.randint(1, 100)

# Define a function that prompts the user for their guess and returns it
def get_user_guess():
    guess = input("Enter your guess (or 'q' to quit): ")
    return guess

# Define a function that checks if the user's guess is correct and returns a message
def check_guess(guess, number):
    if guess == number:
        return "Congratulations! You guessed the number!"
    elif guess < number:
        return "Your guess is too low."
    else:
        return "Your guess is too high."

# Define the main game function
def guess_the_number():
    print("Welcome to Guess the Number Game!")
    print("I am thinking of a number between 1 and 100.")
    print("Try to guess the number.")
    
    # Generate a random number and initialize variables
    number = generate_random_number()
    tries = 0
    high_score = None
    
    while True:
        # Prompt the user for their guess and check if they want to quit
        guess = get_user_guess()
        if guess == 'q':
            print("Better luck next time!")
            break
        
        # Convert the guess to an integer and check if it's correct
        guess = int(guess)
        tries += 1
        message = check_guess(guess, number)
        print(message)
        
        # Update the high score if the user guessed the number in fewer tries
        if high_score is None or tries < high_score:
            high_score = tries
            
        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print(f"Your high score is {high_score}!")
            break

# Call the main game function
guess_the_number()
